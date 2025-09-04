all: program

program: main.o open_file.o gpio.o usart.o
	 g++ main.o open_file.o gpio.o usart.o -o main

main.o: main.cpp main.h
	g++ -c main.cpp -o main.o

open_file.o: open_file.cpp open_file.h
	g++ -c open_file.cpp -o open_file.o

gpio.o: gpio.h gpio.cpp
	g++ -c gpio.cpp -o gpio.o

usart.o: usart.h usart.cpp
	g++ -c usart.cpp -o usart.o

open_file_test: OpenFileTest.o open_file.o user_utils.o
	g++ OpenFileTest.o open_file.o user_utils.o -o test
	sudo chmod +x test
	sudo ./test

OpenFileTest.o: OpenFileTest.h OpenFileTest.cpp
	g++ -c OpenFileTest.cpp -o OpenFileTest.o

user_utils.o: user_utils.h user_utils.cpp
	g++ -c user_utils.cpp -o user_utils.o


clean:
	rm *.o

