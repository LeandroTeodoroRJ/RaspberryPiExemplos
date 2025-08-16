// ACTIVATING GPIO OUTPUT

#include <iostream>
#include <cstdio>
#include <thread>
#include <chrono>

using namespace std;

#define LOW_LEVEL '0'
#define HIGH_LEVEL '1'

FILE *file_to_open;

void pin_gpio4(char level){
	file_to_open = fopen("/mnt/ramdisk/gpio4", "r+");
	if (file_to_open == NULL){
		cout << "File not open." << endl;
	}else{
		cout << "File open" << endl;
		fputc(level, file_to_open);
		fclose(file_to_open);
	}
}


int main(){
	pin_gpio4(HIGH_LEVEL);
	this_thread::sleep_for(chrono::milliseconds(5000));
	pin_gpio4(LOW_LEVEL);
	return 0;
}
