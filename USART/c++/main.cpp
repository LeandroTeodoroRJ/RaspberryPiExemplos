#include "main.h"

using namespace std;

int main(){
	cout << "USART Application." << endl;

/*
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
*/

	Usart usart1;
	printf("USART is idle  Method: %d\n", usart1.is_idle());
	printf("Byte Send Method: %d\n", usart1.send_byte(0xFF));

	return 0;
}

