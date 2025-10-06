import smbus
import time

# Define the I2C bus number
bus_number = 1
bus = smbus.SMBus(bus_number)

# Define the I2C address of your slave device
# Replace with your device's address, see in the manual
device_address = 0x68

# Example: Writing a byte to a register
try:
    register_address = 0x01
    data_to_write = 0x10
    bus.write_byte_data(device_address, register_address, data_to_write)
    print(f"Successfully wrote {hex(data_to_write)} to register {hex(register_address)} on device {hex(device_address)}")
except IOError:
    print(f"Error writing to I2C device at address {hex(device_address)}")

time.sleep(0.01)

# Reading a byte from a register
register_address = 0x01  #Minutes
try:
    read_data = bus.read_byte_data(device_address, register_address)
    print(f"Successfully read {hex(read_data)} from register {hex(register_address)} on device {hex(device_address)}")
except IOError:
    print(f"Error reading from I2C device at address {hex(device_address)}")

register_address = 0x00  #Seconds
try:
    read_data = bus.read_byte_data(device_address, register_address)
    print(f"Successfully read {hex(read_data)} from register {hex(register_address)} on device {hex(device_address)}")
except IOError:
    print(f"Error reading from I2C device at address {hex(device_address)}")
