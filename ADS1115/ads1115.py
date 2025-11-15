'''
 * Description: Example to read continuos analog CH0 - ADS1115.
 * Hostpage: https://github.com/LeandroTeodoroRJ
 * Version: 1.0.0
 * Dependences: ADS1x15-ADC
 * Maintainer: leandroteodoro.enganharia@gmail.com
 * Architecture: Raspberry PI 2W
 * Compile/Interpreter: Python 3.11.2
 * Notes:
	Reference: https://github.com/chandrawi/ADS1x15-ADC
'''

import os
import time
import ADS1x15

MAX_VOLTAGE = 4.096
CHANNEL_ADC_0 = 0

ADS = ADS1x15.ADS1115(1, 0x48)

ADS.setGain(ADS.PGA_4_096V)
ADS.setDataRate(ADS.DR_ADS111X_128)
ADS.setMode(ADS.MODE_CONTINUOUS)
ADS.requestADC(CHANNEL_ADC_0)

while True :
	raw = ADS.getValue()
	voltage = ADS.toVoltage(raw)
	rel_scale = voltage / MAX_VOLTAGE
	print("\nConvert value: ", raw)
	print("Realative scale: ", rel_scale)
	print("Voltage: {0:.3f} V".format(voltage))
	time.sleep(1)


