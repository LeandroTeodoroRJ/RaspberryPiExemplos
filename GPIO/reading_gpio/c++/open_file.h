/*
 * Description: Raspberry Ramdisk files library
 * Hostpage: https://github.com/LeandroTeodoroRJ
 * Version: 1.0.0
 * Dependences: No
 * Maintainer: leandroteodoro.enganharia@gmail.com
 * Architecture: Raspberry PI 2W
 * Compile/Interpreter: g++ 12.2.0
 */

#ifndef OPEN_FILE_H
#define OPEN_FILE_H

#include <iostream>
#include <cstdio>

#define FILE_NOT_OPEN false
#define FILE_OPEN true
#define HIGH_VALUE '1'
#define LOW_VALUE '0'

using namespace std;

class RamdiskFile{
	private:
	protected:
		string file_path;
		FILE *file_to_open;
	public:
		RamdiskFile(string path);
		~RamdiskFile();
		bool file_open();
		void write_high();
		void write_low();
		void file_close();
		char read_unique_value();
};

#endif	/* OPEN_FILE_H */
