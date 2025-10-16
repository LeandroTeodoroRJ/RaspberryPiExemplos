{$H+}   //String is an AnsiString

program TCP_Client(output);
uses
	sockets;

var
	sock_fd: longint;
	saddr: TSockAddr;
	buffer: array[0..255] of byte;
	bytes_sent, bytes_received: longint;
    tcp_message: string;
    tcp_received: string;

begin
tcp_message := 'Free Pascal Hello Server';

// Set up server address
saddr.sin_family := AF_INET;
saddr.sin_port := htons(1300); // Replace with your server's port
saddr.sin_addr := StrToNetAddr('127.0.0.1'); // Replace with your server's IP

// Create socket
sock_fd := fpSocket(AF_INET, SOCK_STREAM, 0);
if sock_fd < 0 then
begin
    writeln('Error creating socket');
    exit;
end;

// Connect to server
if fpConnect(sock_fd, @saddr, sizeof(saddr)) <> 0 then
begin
    writeln('Error connecting to server');
    CloseSocket(sock_fd);
    exit;
end;

// Send data
bytes_sent := fpSend(sock_fd, PChar(tcp_message), Length(tcp_message), 0);
if bytes_sent < 0 then
begin
    writeln('Error sending data');
end;

// Receive data
bytes_received := fpRecv(sock_fd, @buffer, sizeof(buffer), 0);
if bytes_received > 0 then
begin
    tcp_received := PChar(@buffer);
    writeln('Message Received: ', tcp_received);
end;

// Close socket
CloseSocket(sock_fd);

end.
