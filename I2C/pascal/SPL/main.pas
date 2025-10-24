{
 * Description: App to read the seconds I2C TinyRTC module by TCP network loopback.
 * Hostpage: https://github.com/LeandroTeodoroRJ
 * Version: 1.0.0
 * Dependences: python I2C TCP service, sockets, SysUtils
 * Maintainer: leandroteodoro.enganharia@gmail.com
 * Architecture: Raspberry PI 2W
 * Compile/Interpreter: Free Pascal version 1.0.12
}

{$H+}   //String is an AnsiString

program main(output);

uses
	sockets,
    Crt,
    SysUtils;

var
    //TCP Client
	sock_fd: longint;
	saddr: TSockAddr;
	buffer: array[0..255] of byte;
	bytes_sent, bytes_received: longint;
    tcp_message: string;
    tcp_received: string;

    //I2C
    i2c_frame: array[0..100] of integer;
    i2c_frame_lenght: integer;

    //Tiny RTC
    seconds: integer;

//TCP Clients
procedure tcp_connect(port: integer; ip_address: string);
begin
    // Set up server address
    saddr.sin_family := AF_INET;
    saddr.sin_port := htons(port); // Replace with your server's port
    saddr.sin_addr := StrToNetAddr(ip_address); // Replace with your server's IP

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
end;

procedure tcp_send_data;
begin
    // Send data
    bytes_sent := fpSend(sock_fd, PChar(tcp_message), Length(tcp_message), 0);
    if bytes_sent < 0 then
    begin
        writeln('Error sending data');
    end;
end;

procedure tcp_receive_data;
begin
    // Receive data
    bytes_received := fpRecv(sock_fd, @buffer, sizeof(buffer), 0);
    if bytes_received > 0 then
    begin
        tcp_received := PChar(@buffer);
    end;
end;

procedure tcp_close_socket;
begin
    // Close socket
    CloseSocket(sock_fd);
end;

procedure i2c_add_data(data: integer);
begin
    i2c_frame[i2c_frame_lenght]:=  data;
    i2c_frame_lenght:= i2c_frame_lenght + 1;
end;

procedure i2c_send_data_frame(frame_type: string);
var
    send_data_frame: string;
    i: integer;
begin
    i:= 0;
    if frame_type = 'read' then
    begin
        writeln('Read frame');
        send_data_frame:= 'r';
        while i < i2c_frame_lenght do
        begin
            send_data_frame:= send_data_frame + ' ' + '0x' + IntToHex(i2c_frame[i], 2);
            i:= i + 1;
        end;
    end
    else if frame_type = 'write' then
    begin
        writeln('Write frame');
        send_data_frame:= 'w';
        while i < i2c_frame_lenght do
        begin
            send_data_frame:= send_data_frame + ' ' + '0x' + IntToHex(i2c_frame[i], 2);
            i:= i + 1;
        end;
    end
    else
    begin
        writeln('Invalid Option');
    end;
    writeln(send_data_frame);
    tcp_message := send_data_frame;
    i2c_frame_lenght:= 0;
end;

//Tiny RTC
function binary_to_time(rtc_sec: integer): integer;
var
    sec_converted: integer;
    low_value: integer;
    high_value: integer;
begin
    low_value:= $0F and rtc_sec;
    high_value:= RolByte($F0 and rtc_sec, 4);
    sec_converted:= high_value*10 + low_value;
    binary_to_time:= sec_converted;
end;

// Start Main Block
begin
    //init
    i2c_frame_lenght:= 0;

    //Read seconds
    tcp_connect(1300, '127.0.0.1');
    i2c_add_data($68);
    i2c_add_data($00);
    i2c_send_data_frame('read');
    tcp_send_data;
    delay(20);
    tcp_receive_data;
    seconds:= binary_to_time(StrToInt(tcp_received));
    tcp_close_socket;

    writeln('The second time is: ', seconds);

end.
