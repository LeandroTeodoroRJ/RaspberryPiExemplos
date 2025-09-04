#include "OpenFileTest.h"

using namespace std;

void test(bool test_result){
	if(test_result == true){
		cout << "Pass" << endl;
	}else{
		cout << "FAIL" << endl;
		exit(1);
	}
}

int main(){

	cout << "1. Write a string into file" << endl;
	RamdiskFile ram_file("/mnt/ramdisk/usart_id");
	ram_file.file_open();
	string text_to_write = "Message in file";
	ram_file.write_str(text_to_write);
	ram_file.file_close();
	test(return_one_line_command_os("cat /mnt/ramdisk/usart_id") == text_to_write);

	cout << "2. Read a frist line of the file" << endl;
	ram_file.file_open();
	test(ram_file.read_frist_line_str() == text_to_write);
	ram_file.file_close();

	return 0;
}

