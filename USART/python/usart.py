'''
 * Description: Module to acess usart by file.
 * Hostpage: https://github.com/LeandroTeodoroRJ
 * Version: 1.0.1
 * Dependences: --
 * Maintainer: leandroteodoro.enganharia@gmail.com
 * Architecture: Raspberry PI 2W
 * Compile/Interpreter: Python 3.11.2
 * Notes:
'''


# TRANSMITTER BY FILE

import time
import os
import random

class Usart:
	USART_IS_FREE = "0"
	USART_IS_TRANSMITTING_NOW = "1"
	ERROR_BYTE_NOT_SEND = 1
	ERROR_USART_NOT_FREE = 2
	ERROR_USART_TRANSMITTING = 3
	BYTE_WAS_SEND = 0

	def __init__(self):
		self.bytes_to_transmitter = []
		self.buffer_received = []

	def send_buffer(self):
		if (self.is_idle() == False):
			return self.ERROR_USART_NOT_FREE
		if (self.is_transmitting == True):
			return self.ERROR_USART_TRANSMITTING
		self.str_byte = str()

		# Request TX
		with open("/mnt/ramdisk/usart_idle_tx", "w") as file:
			file.write("1")

		# Putting App transaction code
		with open("/mnt/ramdisk/usart_id", "w") as file:
			file.write("12345")

		# Writing data to transfer
		for i in self.bytes_to_transmitter:
			self.str_byte = self.str_byte + " " + i
		with open("/mnt/ramdisk/usart_tx_buffer", "w") as file:
			file.write(self.str_byte[1::])
			self.bytes_to_transmitter = []

		# Enable to transfer
		with open("/mnt/ramdisk/usart_tx_send", "w") as file:
			file.write("1")

		time.sleep(0.2)

		# Putting TX is free
		with open("/mnt/ramdisk/usart_idle_tx", "w") as file:
			file.write("0")


	def receiver_bytes(self):
		if (self.was_received_bytes() == False):
			return 1

		with open("/mnt/ramdisk/usart_rx_buffer", "r") as file:
			self.data_read = file.read()
			self.data_read = self.data_read.replace(" ","")
			self.number_bytes_received = int(len(self.data_read)/2)
			self.i = 0
			self.buffer_received = []
			while(self.i < len(self.data_read)):
				self.buffer_received.append(int("0x" + self.data_read[self.i]+self.data_read[self.i+1], 16))
				self.i = self.i + 2

		# USART RX is free
		with open("/mnt/ramdisk/usart_rx", "w") as file:
			file.write("0")

	def is_idle(self):
		with open("/mnt/ramdisk/usart_idle_tx", "r") as file:
			self.is_free = file.read()
			if (self.is_free[0] == self.USART_IS_FREE):
				return True
			else:
				return False


	def is_transmitting(self):
		with open("/mnt/ramdisk/usart_tx_send", "r") as file:
			self.is_tx = file.read()
		if (self.is_tx[0] == self.USART_IS_TRANSMITTING_NOW):
			return True
		else:
			return False


	def add_byte_to_transmitter(self, byte):
		if (byte <= 0xF):
			if (byte == 0x00):
				self.bytes_to_transmitter.append("00")
			else:
				self.bytes_to_transmitter.append("0" + str(hex(byte))[2::].upper())
		else:
			self.bytes_to_transmitter.append(str(hex(byte))[2::].upper())

	def was_received_bytes(self):
		with open("/mnt/ramdisk/usart_rx", "r") as file:
			self.received = file.read()
			try:
				if (self.received[0] == "1"): 
					return True
				else:
					return False
			except IndexError:
				return False


