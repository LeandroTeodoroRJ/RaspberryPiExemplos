import serial

ser = serial.Serial('/dev/serial0')
ser.baud = 115200
ser.parity = serial.PARITY_NONE
ser.stopbits = serial.STOPBITS_ONE
ser.bytesize = serial.EIGHTBITS
ser.timeout = 1

hexa_num = '0F'
data = bytes.fromhex(hexa_num)
ser.write(data)

hexa_num = '5A'
data = bytes.fromhex(hexa_num)
ser.write(data)

ser.close()

