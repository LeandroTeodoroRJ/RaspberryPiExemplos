/*
 * Description: Library to USART acess by Ramdisk files
 * Hostpage: https://github.com/LeandroTeodoroRJ
 * Version: 1.0.0
 * Dependences: open_file.h
 * Maintainer: leandroteodoro.enganharia@gmail.com
 * Architecture: Raspberry PI 2W
 * Compile/Interpreter: g++ 12.2.0
 * TODO:
	-- Create ramdom usart ID code.
 	-- Decrease delay to transmitter.
	-- Replace delay to transmitter to check usart_tx_send
 */


#ifndef USART_H
#define USART_H

#include <iostream>
#include <cstdio>
#include "open_file.h"
#include <thread>
#include <chrono>
#include <sstream>
#include <ctype.h>

#define USART_IS_FREE '0'
#define USART_NOT_TRANSMITTING '0'
#define BYTE_WAS_SEND false
#define ERROR_BYTE_NOT_SEND true
#define DELAY_TO_SEND 2000
#define BYTE_NOT_RECEIVED false

class Usart{
	private:
	protected:
		int bytes_to_transmitter;
		int buffer_tx[256];		//Modify to application maximum dataframe
		int buffer_tx_position = 0;
		int buffer_rx_position = 0;
	public:
		int number_bytes_received;
		int buffer_rx[256];
		Usart();
		~Usart();
		int id_code_generator();
		bool is_idle();
		bool is_transmitting();
		bool send_byte(int byte_to_send);
		void in_use();
		void free_to_other_request();
		void write_tx_id_code();
		void transmitter_now();
		string convert_byte_to_str(int byte);
		bool send_buffer();
		void add_byte_to_send(int byte);
		bool was_received_byte();
		bool receiver_bytes();
		void confirm_message_received();
};

#endif	//USART_H
