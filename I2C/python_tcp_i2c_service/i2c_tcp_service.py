'''
 * Description: Service to acsess I2C hardware rasponse to TCP network loopback.
 * Hostpage: https://github.com/LeandroTeodoroRJ
 * Version: 1.0.0
 * Dependences: pyserial 3.5
 * Maintainer: leandroteodoro.enganharia@gmail.com
 * Architecture: Raspberry PI 2W
 * Compile/Interpreter: Python 3.11.2
 * Referências:
https://docs.python.org/3/library/socket.html
https://realpython.com/python-sockets/
'''

import socket
import time
import smbus
import os

PORT = 1300

servidor = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#AF_INET -> IP V4 Protocol
#SOCK_TREAM -> TCP
#SOCK_DGRAM -> UDP

servidor.bind(('0.0.0.0', PORT))
servidor.listen()

# Define the I2C bus number
bus_number = 1
bus = smbus.SMBus(bus_number)

def transmitter_data_to_tcp(data_to_transmitter):
	conn.sendall(data_to_transmitter)               #Return to the client

def receive_data_from_tcp(data_received):
	str_data = data_received.decode("utf-8")
	str_slice_list = str_data.split(' ')
	if (str_slice_list[0] == "w"):
		del(str_slice_list[0])
		bus.write_byte_data(int(str_slice_list[0], 16), int(str_slice_list[1], 16), int(str_slice_list[2], 16))
	elif (str_slice_list[0] == "r"):
		del(str_slice_list[0])
		read_data = bus.read_byte_data(int(str_slice_list[0], 16), int(str_slice_list[1], 16))
		transmitter_str = bytes(str(read_data), "utf-8")
		transmitter_data_to_tcp(transmitter_str)
	else:
		invalid_option_error = "Invalid option error - IP: " + str(addr)
		command = "sudo echo \"" + invalid_option_error + "-$(date)\" >> /home/pi/Dev/I2C/python_tcp_i2c_service/error.log"
		os.system(command)


while True:
	conn, addr = servidor.accept()     #conn is a socket object
	with conn:
		data = conn.recv(1024)         #Receiver max 1024 bytes of buffer
		if not data:                   #If nothing is received close the socket
			conn.close()               #... but the listen port is active
			continue
		else:							#If any bytes was received
			receive_data_from_tcp(data)
#			print('Connected to IP: ', addr)
			time.sleep(0.01)              #Delay 10ms
			conn.close()                #Stop communication
