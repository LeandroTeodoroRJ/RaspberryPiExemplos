from gpio import Button
from usart import Usart
import time

button17 = Button("/mnt/ramdisk/gpio17")
button27 = Button("/mnt/ramdisk/gpio27")
usart1 = Usart()
DEVICE_ADDRESS = 0X21


def send_message_to_other_device():
	usart1.add_byte_to_transmitter(0x17)
	usart1.add_byte_to_transmitter(0x05)
	usart1.add_byte_to_transmitter(0x01)
	usart1.send_buffer()


def send_message_to_this_device():
	usart1.add_byte_to_transmitter(DEVICE_ADDRESS)
	usart1.add_byte_to_transmitter(0x04)
	usart1.add_byte_to_transmitter(0xA2)
	usart1.send_buffer()


def usart_events():
	if (usart1.buffer_received != []):
		print("Buffer received: ", usart1.buffer_received)
		if (usart1.buffer_received[0] == DEVICE_ADDRESS):
			print("This message for me.")
		else:
			print("This message is not for me.")
		usart1.buffer_received = []


while True:
	button17.key_scan()
	button27.key_scan()
	if (button17.is_clicked() == True):
		send_message_to_this_device()
		button17.event_end()
	if (button27.is_clicked() == True):
		send_message_to_other_device()
		button27.event_end()
	usart1.receiver_bytes()
	usart_events()
	time.sleep(0.03)

