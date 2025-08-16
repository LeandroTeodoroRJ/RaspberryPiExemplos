#include <iostream>
#include "main.h"

using namespace std;

int main(){
	cout << "Reading GPIO Input" << endl;

	GpioPin button1(INPUT_MODE, "/mnt/ramdisk/gpio17");
	GpioPin led(OUTPUT_MODE, "/mnt/ramdisk/gpio4");

	while (true){
		if (button1.get_pin_value() == BUTTON_PRESSED){
			led.set_pin_value(PIN_HIGH_VALUE);
		}else{
			led.set_pin_value(PIN_LOW_VALUE);
		}
		this_thread::sleep_for(chrono::milliseconds(100));
	}

	return 0;
}

