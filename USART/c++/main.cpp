#include "main.h"

using namespace std;

int main(){
	cout << "USART Application." << endl;

	Usart usart1;
/*
	cout << "USART trasmitter byte" << endl;
	printf("Byte Send Method: %d\n", usart1.send_byte(0xFA));
*/

	cout << "USART trasmitter buffer" << endl;
	usart1.add_byte_to_send(0xDD);
	usart1.add_byte_to_send(0xEE);
	usart1.add_byte_to_send(0xFF);
	usart1.send_buffer();


	cout << "USART receiver buffer" << endl;
	if (usart1.receiver_bytes() == true){
		for (int i = 0; i < usart1.number_bytes_received; i++){
			cout << "Received bytes: " << usart1.buffer_rx[i] << endl;
		}
	}

	return 0;
}

