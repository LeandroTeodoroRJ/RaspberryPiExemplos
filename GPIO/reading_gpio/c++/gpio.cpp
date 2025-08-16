#include "gpio.h"

using namespace std;

GpioPin::GpioPin(bool pin_mode, string path){
	mode = pin_mode;
	pin_file_path = path;
}

GpioPin::~GpioPin(){

}

bool GpioPin::get_pin_value(){
	if (mode == INPUT_MODE){
		char ch_value;
		RamdiskFile GPIO_file(pin_file_path);
		GPIO_file.file_open();
		ch_value = GPIO_file.read_unique_value();
		GPIO_file.file_close();
		return ch_value - '0';
	}else{
		return status;
	}
}

void GpioPin::set_pin_value(bool value){
	if (mode == OUTPUT_MODE){
		RamdiskFile GPIO_file(pin_file_path);
		GPIO_file.file_open();
		if (value == PIN_HIGH_VALUE){
			GPIO_file.write_high();
			status = PIN_HIGH_VALUE;
		}else{
			GPIO_file.write_low();
			status = PIN_LOW_VALUE;
		}
		GPIO_file.file_close();
	}
}

