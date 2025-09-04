/*
 * Description: Library to USART acess by Ramdisk files
 * Hostpage: https://github.com/LeandroTeodoroRJ
 * Version: 1.0.0
 * Dependences: open_file.h
 * Maintainer: leandroteodoro.enganharia@gmail.com
 * Architecture: Raspberry PI 2W
 * Compile/Interpreter: g++ 12.2.0
 */


#ifndef USART_H
#define USART_H

#include <iostream>
#include <cstdio>
#include "open_file.h"
#include <thread>
#include <chrono>

#define USART_IS_FREE '0'
#define BYTE_WAS_SEND false
#define ERROR_BYTE_NOT_SEND true

class Usart{
	private:
	protected:
	public:
		Usart();
		~Usart();
		int id_code_generator();
		bool is_idle();
		bool send_byte(int byte_to_send);
		void in_use();
		void free_to_other_request();
		void write_tx_id_code();
		void transmitter_now();
};

#endif	//USART_H
