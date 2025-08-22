with open("/mnt/ramdisk/usart_rx", "r") as file:
	file_data = file.read()
	print("usart_rx is "+file_data)

with open("/mnt/ramdisk/usart_rx_buffer", "r") as file:
	file_data = file.read()
	print("The rx buffer is "+file_data)


print("USART RX is free")
with open("/mnt/ramdisk/usart_rx", "w") as file:
	file.write("0")

