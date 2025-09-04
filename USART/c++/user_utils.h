#ifndef USERUTILS_H
#define USERUTILS_H

#include <iostream>
#include <cstdio>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

using namespace std;

/*
Return the terminal result (01 line only) of the
Operational System command line.
Example:
    string exec = "ls -l";
    string result_command = return_one_line_command_os(exec);
    cout <<  result_command;

*/
string return_one_line_command_os(string command);


#endif
