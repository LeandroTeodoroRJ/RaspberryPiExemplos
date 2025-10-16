#include <iostream>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <unistd.h>
#include <string>

using namespace std;

int main() {
    // 1. Create a socket
    int clientSocket = socket(AF_INET, SOCK_STREAM, 0);  //AF_INET - IPv4; SOCK_STREAM - TCP
    if (clientSocket == -1) {
        cerr << "Error creating socket." << endl;
        return 1;
    }

    // 2. Define server address
    sockaddr_in serverAddress;
    serverAddress.sin_family = AF_INET;
    serverAddress.sin_port = htons(1300); // Server port
    serverAddress.sin_addr.s_addr = inet_addr("127.0.0.1"); // Server IP

    // 3. Connect to the server
    if (connect(clientSocket, (struct sockaddr*)&serverAddress, sizeof(serverAddress)) == -1) {
        cerr << "Error connecting to server." << endl;
        close(clientSocket);
        return 1;
    }
    cout << "Connected to server." << endl;

    // 4. Send data
    string message = "Hello from C++ client!";
    send(clientSocket, message.c_str(), message.length(), 0);
    cout << "Sent: " << message << endl;

    // 5. Receive data
    char buffer[1024] = {0};
    recv(clientSocket, buffer, 1024, 0);
	if (buffer[0] == 0){
		cout << "Nothing to receiver" << endl;
	}else{
	    cout << "Received from server: " << buffer << endl;
	}


    // 6. Close the socket
    close(clientSocket);
    return 0;
}
