#include "usart.h"

using namespace std;


Usart::Usart(){

}

Usart::~Usart(){

}


int Usart::id_code_generator(){
	int code = 123;
	return code;
}


bool Usart::is_idle(){
	char check_busy;
	RamdiskFile idle("/mnt/ramdisk/usart_idle_tx");
	idle.file_open();
	check_busy = idle.read_unique_value();
	idle.file_close();
	if (check_busy == USART_IS_FREE){
		return true;
	}else{
		return false;
	}
}

bool Usart::send_byte(int byte_to_send){
	//Check usart_idle_tx is free
	if (this->is_idle() == false){
		return ERROR_BYTE_NOT_SEND;
	}
	//Check usart_tx_send 0
	//Write usart_idle_tx 1
	this->in_use();
	//Write usart_id_code
	this->write_tx_id_code();
	//write usart_tx_buffer
		//Test
		RamdiskFile idle("/mnt/ramdisk/usart_tx_buffer");
		idle.file_open();
		idle.write_str("55 55 55");
		idle.file_close();
	//write_tx_send 1
	this->transmitter_now();
	//Wait to trasmitter
	this_thread::sleep_for(chrono::milliseconds(2000));
	//write usart_idle_tx 0
	this->free_to_other_request();
	return BYTE_WAS_SEND;
}


void Usart::in_use(){
	RamdiskFile idle("/mnt/ramdisk/usart_idle_tx");
	idle.file_open();
	idle.write_high();
	idle.file_close();
}


void Usart::free_to_other_request(){
	RamdiskFile idle("/mnt/ramdisk/usart_idle_tx");
	idle.file_open();
	idle.write_low();
	idle.file_close();
}


void Usart::write_tx_id_code(){
	string code = to_string(this->id_code_generator());
	RamdiskFile idle("/mnt/ramdisk/usart_id");
	idle.create_blank_file();
	idle.file_open();
	idle.write_str(code);
	idle.file_close();
}

void Usart::transmitter_now(){
	RamdiskFile idle("/mnt/ramdisk/usart_tx_send");
	idle.file_open();
	idle.write_high();
	idle.file_close();
}
