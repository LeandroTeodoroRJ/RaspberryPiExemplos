#include "open_file.h"

using namespace std;

RamdiskFile::RamdiskFile(string path){
	file_path = path;
}

RamdiskFile::~RamdiskFile(){

}

bool RamdiskFile::file_open(){
	file_to_open = fopen(file_path.c_str(), "r+");
	if (file_to_open == NULL){
		return FILE_NOT_OPEN;
	}else{
		return FILE_OPEN;
	}
}

void RamdiskFile::write_high(){
	fputc('1', file_to_open);
}

void RamdiskFile::write_low(){
	fputc('0', file_to_open);
}

void RamdiskFile::file_close(){
	fclose(file_to_open);
}

char RamdiskFile::read_unique_value(){
	char value;
	fread(&value, sizeof(char), 1, file_to_open);
	return value;
}
