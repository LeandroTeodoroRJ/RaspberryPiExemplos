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

void RamdiskFile::write_str(string text){
	int str_len = text.size();
	for (int i = 0; i < str_len; i++){
		fputc(text[i], file_to_open);
	}
}

string RamdiskFile::read_frist_line_str(){
	char buffer[256];
	fgets(buffer, sizeof(buffer), file_to_open);
    buffer[strcspn(buffer, "\r\n")] = 0;
 	string result(buffer);
	return result;
}

void RamdiskFile::create_blank_file(){
	string file_blank_path = "> " + this->file_path;
	system(file_blank_path.c_str());
}
