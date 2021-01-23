# Exemplo de uso da interface SPI
# Raspberry Pi3 Model B+

import spidev
spi = spidev.SpiDev()
bus = 0
device = 0
spi.open(bus, device)
spi.max_speed_hz = 5000
spi.mode = 0b01
to_send = [0x55, 0x10]
spi.xfer(to_send)
spi.close()

