'''
 * Description: Module to acess gpio by file.
 * Hostpage: https://github.com/LeandroTeodoroRJ
 * Version: 1.0.0
 * Dependences: --
 * Maintainer: leandroteodoro.enganharia@gmail.com
 * Architecture: Raspberry PI 2W
 * Compile/Interpreter: Python 3.11.2
 * Notes:
'''

class Button:
	def __init__(self, full_path):
		self.path = full_path
		self.is_pressed = False
		self.button_click = False

	def event_end(self):
		self.is_pressed = False

	def is_clicked(self):
		if (self.is_pressed == True):
			if (self.button_click == False):
				self.button_click = True
				return True
		else:
			self.button_click = False
			return False


	def key_scan(self):
		with open(self.path, "r") as file:
			self.data = file.read()
			try:
				if (self.data[0] == "0"):
					self.is_pressed = True
				else:
					self.is_pressed = False
			except IndexError:
				self.is_pressed = False


