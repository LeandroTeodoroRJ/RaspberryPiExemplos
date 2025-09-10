'''
 * Description: Service to acsess USART hardware.
 * Hostpage: https://github.com/LeandroTeodoroRJ
 * Version: 1.0.0
 * Dependences: pyserial 3.5
 * Maintainer: leandroteodoro.enganharia@gmail.com
 * Architecture: Raspberry PI 2W
 * Compile/Interpreter: Python 3.11.2
 * Notes:
	-- Install PySerial:
		python3 -m venv py_usart_venv
		pip3 install pyserial
	-- Don't forget deactivate serial port to use with shell in raspi-config.
	   (Serial - Enable / Serial Shell - Disable)
'''

import os
import serial
import time

BAUD_RATE = 115200
DELAY_POOLING = 0.05
TIME_TO_RECEIVER_RESPONSE = 10000
TIME_TO_TRANSMITTER_LET_FREE = 10000

time_out_timer = 0
id_rx_code = " "
time_out_tx = 0

ser = serial.Serial('/dev/serial0')
ser.baud = BAUD_RATE
ser.parity = serial.PARITY_NONE
ser.stopbits = serial.STOPBITS_ONE
ser.bytesize = serial.EIGHTBITS
ser.timeout = 1

# TRANSMITTER
def create_usart_tx_file_blank():
	os.system("> /mnt/ramdisk/usart_tx_buffer")

def create_usart_id_file_blank():
	os.system("> /mnt/ramdisk/usart_id")

def create_usart_idle():
	os.system("touch /mnt/ramdisk/usart_idle_tx")
	os.system("echo 0 > /mnt/ramdisk/usart_idle_tx")

def create_usart_tx_send():
	os.system("touch /mnt/ramdisk/usart_tx_send")
	os.system("echo 0 > /mnt/ramdisk/usart_tx_send")

def usart_tx_is_request():
	with open("/mnt/ramdisk/usart_idle_tx", "r") as file:
		file_data = file.read()
		frist_char_file = file_data[0]
		if (frist_char_file == "1"):
			return True
		else:
			return False

def usart_tx_is_ready_to_send():
	with open("/mnt/ramdisk/usart_tx_send", "r") as file:
		file_data = file.read()
		frist_char_file = file_data[0]
		if (frist_char_file == "1"):
			return True
		else:
			return False

def read_bytes_to_transmitter():
	bytes_to_send = ''
	with open("/mnt/ramdisk/usart_tx_buffer", "r") as file:
		file_data = file.read()
	for i in file_data:
		if (i != ' '):
			bytes_to_send += i
	return bytes_to_send

def read_id_tx_code():
	with open("/mnt/ramdisk/usart_id", "r") as file:
		file_data = file.read()
	return file_data


def transmitter_bytes():
	if (usart_tx_is_request() != True):
		return 0
	if (usart_tx_is_ready_to_send() != True):
		return 0
	str_message = read_bytes_to_transmitter()
	i = 0
	while (i < len(str_message)):
		byte_to_send = str_message[i]
		byte_to_send += str_message[i+1]
		i += 2
		data = bytes.fromhex(byte_to_send)
		ser.write(data)
	create_usart_tx_file_blank()
	create_usart_tx_send()
	global id_rx_code
	id_rx_code = read_id_tx_code()

def transmitter_response_time_out():
	global time_out_tx
	if (usart_tx_is_request() != True):
		return 0
	if (id_rx_code == read_id_tx_code()):
		if (time_out_tx > TIME_TO_TRANSMITTER_LET_FREE):
			time_out_tx = 0
			create_usart_idle()
		else:
			time_out_tx += 1
	else:
		time_out_tx = 0



# RECEIVER
def create_usart_rx_file_blank():
	os.system("> /mnt/ramdisk/usart_rx_buffer")

def create_usart_rx():
	os.system("touch /mnt/ramdisk/usart_rx")
	os.system("echo 0 > /mnt/ramdisk/usart_rx")

def usart_rx_free():
	os.system("echo 0 > /mnt/ramdisk/usart_rx")

def byte_to_string(byte_list):
	str_list = []
	for i in byte_list:
		str_list.append(str(i.hex()).upper())
	return str_list

def save_usart_rx_buffer(str_list):
	with open("/mnt/ramdisk/usart_rx_buffer", "w") as file:
		for i in str_list:
			file.write(i)
			file.write(" ")

def usart_received_new_byte():
	with open("/mnt/ramdisk/usart_rx", "w") as file:
		file.write("1")

def usart_rx_is_free():
	with open("/mnt/ramdisk/usart_rx", "r") as file:
		file_data = file.read()
		frist_char_file = file_data[0]
		if (frist_char_file == "0"):
			return True
		else:
			return False


def receiver_bytes():
	if (usart_rx_is_free() != True):
		return 0
	byte_received = ser.read()
	if (byte_received == b''): #Nothing Received
		return 0
	buffer_rx = []
	buffer_rx.append(byte_received)
	byte_received = ser.read()
	while (byte_received != b''):
		buffer_rx.append(byte_received)
		byte_received = ser.read()
	buffer_rx = byte_to_string(buffer_rx)
	create_usart_rx_file_blank()
	save_usart_rx_buffer(buffer_rx)
	usart_received_new_byte()

def receiver_time_out_response():
	global time_out_timer
	if (usart_rx_is_free() == True):
		time_out_timer = 0
		return 0
	time_out_timer += 1
	if ( time_out_timer > TIME_TO_RECEIVER_RESPONSE):
		time_out_timer = 0
		create_usart_rx()


# MAIN
create_usart_rx_file_blank()
create_usart_rx()
create_usart_tx_file_blank()
create_usart_id_file_blank()
create_usart_idle()
create_usart_tx_send()
while True:
	receiver_bytes()
	receiver_time_out_response()
	transmitter_bytes()
	transmitter_response_time_out()
	time.sleep(DELAY_POOLING)
