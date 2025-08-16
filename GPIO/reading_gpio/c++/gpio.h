/*
 * Description: Acess GPIO pins using ramdisk files.
 * Hostpage: https://github.com/LeandroTeodoroRJ
 * Version: 1.0.0
 * Dependences: open_file ver:1.0.0
 * Maintainer: leandroteodoro.enganharia@gmail.com
 * Architecture: Raspberry PI 2W
 * Compile/Interpreter: g++ 12.2.0
 */

#ifndef GPIO_H
#define GPIO_H

#include <iostream>
#include <cstdio>
#include "open_file.h"

#define BUTTON_PRESSED 0
#define BUTTON_NOT_PRESSED 1
#define INPUT_MODE 1
#define OUTPUT_MODE 0
#define PIN_HIGH_VALUE 1
#define PIN_LOW_VALUE 0

using namespace std;

class GpioPin{
	private:
	protected:
		bool mode;
		bool status;
		string pin_file_path;
	public:
		GpioPin(bool pin_mode, string path);
		~GpioPin();
		bool get_pin_value();
		void set_pin_value(bool value);
};

#endif	/* GPIO_H */
