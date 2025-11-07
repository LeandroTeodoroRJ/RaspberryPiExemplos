'''
 * Description: How to use the mfrc522 RFID module.
 * Hostpage: https://github.com/LeandroTeodoroRJ
 * Version: 1.0.0
 * Dependences: mfrc522
 * Maintainer: leandroteodoro.enganharia@gmail.com
 * Architecture: Raspberry PI 2W
 * Compile/Interpreter: Python 3.11.2
'''


from time import sleep
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

GPIO.setwarnings(False)  #Disable GPIO runtime warnings

leitorRfid = SimpleMFRC522()

try:
	while True:
		menu = input("Choose an option: \n1 - Read the RFID Card. \n2 - Write the RFID Card. \nAny key - Quit. \n")
		if menu == "1":
			print("\nRead Mode")
			print("----------------------------")
			print("Bring the tag closer to the reader:")
			cardid, text = leitorRfid.read()
			print("ID Card: ", cardid)
			print("Memory Card Data:")
			print(text)
			print("")
			sleep(1)
		elif menu == "2":
			print("\nWrite Mode")
			text = input("Choose the data to memory write: ")
			print("Bring the tag will be to write.")
			leitorRfid.write(text)
			print("Done!\n")
		else:
			print("exiting...")
			exit(1)

except KeyboardInterrupt:
    GPIO.cleanup()  #Clean GPIO set as default (input)
    raise


