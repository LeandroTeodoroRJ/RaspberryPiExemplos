from usart import Usart
import time
import random

i = 0
usart1 = Usart()
while True:
	if (i == 5):
#		usart1.add_byte_to_transmitter(0xAA)
#		usart1.add_byte_to_transmitter(0xBB)
#		usart1.add_byte_to_transmitter(0xCC)

		usart1.add_byte_to_transmitter(random.randint(0, 254))
		usart1.add_byte_to_transmitter(random.randint(0, 254))
		usart1.add_byte_to_transmitter(random.randint(0, 254))
		usart1.add_byte_to_transmitter(random.randint(0, 254))
		usart1.add_byte_to_transmitter(random.randint(0, 254))
		usart1.add_byte_to_transmitter(random.randint(0, 254))
		usart1.add_byte_to_transmitter(random.randint(0, 254))
		usart1.add_byte_to_transmitter(random.randint(0, 254))

		usart1.send_buffer()
		i = 0
	usart1.receiver_bytes()
	if (usart1.buffer_received != []):
		print("Buffer received: ", usart1.buffer_received)
		usart1.buffer_received = []
	i += 1
#	time.sleep(random.uniform(0.5, 1.0))
	time.sleep(0.2)
#	break
