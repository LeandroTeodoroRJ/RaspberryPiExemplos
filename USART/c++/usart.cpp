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


bool Usart::is_transmitting(){
	char check_transmitting_now;
	RamdiskFile usart("/mnt/ramdisk/usart_tx_send");
	usart.file_open();
	check_transmitting_now = usart.read_unique_value();
	usart.file_close();
	if (check_transmitting_now == USART_NOT_TRANSMITTING){
		return false;
	}else{
		return true;
	}
}


bool Usart::send_byte(int byte_to_send){
	//Check usart_idle_tx is free
	if (this->is_idle() == false){
		return ERROR_BYTE_NOT_SEND;
	}
	//Check usart_tx_send 0
	if (this->is_transmitting() == true){
		return ERROR_BYTE_NOT_SEND;
	}
	//Write usart_idle_tx 1
	this->in_use();
	//Write usart_id_code
	this->write_tx_id_code();
	//write usart_tx_buffer
	RamdiskFile usart_comm("/mnt/ramdisk/usart_tx_buffer");
	usart_comm.file_open();
	usart_comm.write_str(this->convert_byte_to_str(byte_to_send));
	usart_comm.file_close();
	//write_tx_send 1
	this->transmitter_now();
	//Wait to trasmitter
	this_thread::sleep_for(chrono::milliseconds(DELAY_TO_SEND));
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

string Usart::convert_byte_to_str(int byte){
	stringstream conv;
	string hexa_str;
	conv << hex <<byte;
	hexa_str = conv.str();
	for (int i = 0; i < hexa_str.length(); i++){
		hexa_str[i] = toupper(hexa_str[i]);
	}
	return hexa_str;
}

void Usart::add_byte_to_send(int byte){
	buffer_tx[buffer_tx_position] = byte;
	buffer_tx_position++;
}

bool Usart::send_buffer(){
	//Check usart_idle_tx is free
	if (this->is_idle() == false){
		return ERROR_BYTE_NOT_SEND;
	}
	//Check usart_tx_send 0
	if (this->is_transmitting() == true){
		return ERROR_BYTE_NOT_SEND;
	}
	//Write usart_idle_tx 1
	this->in_use();
	//Write usart_id_code
	this->write_tx_id_code();
	//write usart_tx_buffer
	RamdiskFile usart_comm("/mnt/ramdisk/usart_tx_buffer");
	usart_comm.file_open();
	for (int i = 0; i < buffer_tx_position; i++){
		usart_comm.write_str(this->convert_byte_to_str(this->buffer_tx[i]) + " ");
	}
	usart_comm.file_close();
	//write_tx_send 1
	this->transmitter_now();
	//Wait to trasmitter
	this_thread::sleep_for(chrono::milliseconds(DELAY_TO_SEND));
	//write usart_idle_tx 0
	this->free_to_other_request();
	buffer_tx_position = 0;
	return BYTE_WAS_SEND;
}

bool Usart::was_received_byte(){
	char check;
	RamdiskFile usart("/mnt/ramdisk/usart_rx");
	usart.file_open();
	check = usart.read_unique_value();
	usart.file_close();
	if (check == '1'){
		return true;
	}else{
		return false;
	}
}

bool Usart::receiver_bytes(){
	if (this->was_received_byte() == false){
		return BYTE_NOT_RECEIVED;
	}
	//read usart buffer
	string not_spaced;
	string str_byte_received;
	RamdiskFile usart_comm("/mnt/ramdisk/usart_rx_buffer");
	usart_comm.file_open();
	string unformated = usart_comm.read_frist_line_str();
	usart_comm.file_close();
	for (char c : unformated){
		if (c != ' '){
			not_spaced += c;
		}
	}
	this->number_bytes_received = (not_spaced.size()/2);
	for(int i = 0; i < not_spaced.size(); i = i+2){
		str_byte_received = not_spaced.substr(i, 2);
		this->buffer_rx[this->buffer_rx_position++] = stoi(str_byte_received, 0, 16);
	}
	this->buffer_rx_position = 0;
	//write usart_rx 1
	this->confirm_message_received();
	return true;
}

void Usart::confirm_message_received(){
	RamdiskFile idle("/mnt/ramdisk/usart_rx");
	idle.file_open();
	idle.write_low();
	idle.file_close();
}
