all: program

program: main.o open_file.o gpio.o
	 g++ main.o open_file.o gpio.o -o main

main.o: main.cpp main.h
	g++ -c main.cpp -o main.o

open_file.o: open_file.cpp open_file.h
	g++ -c open_file.cpp -o open_file.o

gpio.o: gpio.h gpio.cpp
	g++ -c gpio.cpp -o gpio.o

clean:
	rm *.o
