# TRANSMITTER BY FILE

import time

print("Request TX")
with open("/mnt/ramdisk/usart_idle_tx", "w") as file:
	file.write("1")

print("Putting App transaction code")
with open("/mnt/ramdisk/usart_id", "w") as file:
	file.write("12345")

print("Writing data to transfer")
with open("/mnt/ramdisk/usart_tx_buffer", "w") as file:
	file.write("5F B8 10 C4")

print("Enable to transfer")
with open("/mnt/ramdisk/usart_tx_send", "w") as file:
	file.write("1")

time.sleep(2)

'''
print("Putting TX is free")
with open("/mnt/ramdisk/usart_idle_tx", "w") as file:
	file.write("0")
'''
