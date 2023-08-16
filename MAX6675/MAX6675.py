#************************************************************
#        PROGRAMA DESTINADO A CONEXÃO COM MAX6675
#************************************************************
'''
Este programa tem o objetivo de realizar a conectividade da
interface e sensor de temperatura implementado com o
integrado MAX6675 e o termopar tipo K na porta SPI do
Raspiberry Pi3 Model B.
'''

import spidev
import time

spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 3900000

cont = 0

def sensor_read(sample):
	t = spi.readbytes(2)
	time.sleep(sample)

	msb = format(t[0], '#010b')
	lsb = format(t[1], '#010b')

	r_temp = msb[2:] + lsb[2:]
	t_bytes = "0b" + r_temp[0:13]
	temp = int(t_bytes, base=2)*0.25
	return temp


while(cont < 11):
	print("Temperatura: {:.2f} ºC".format(sensor_read(0.5)))
	cont = cont+1




