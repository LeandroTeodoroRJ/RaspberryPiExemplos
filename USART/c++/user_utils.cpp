#include "user_utils.h"
using namespace std;

string return_one_line_command_os(string command){
  char buffer[256];
  FILE *fp;
  int status;

  fp = popen(command.c_str(), "r");

  if (fp == NULL) {
    return "No Value Error";
  }

  fgets(buffer, sizeof(buffer), fp);
  buffer[strcspn(buffer, "\r\n")] = 0;
  status = pclose(fp);

  if (status != 0) {
    return "Error to execute command";
  }
    string result(buffer);
	return result;
}


