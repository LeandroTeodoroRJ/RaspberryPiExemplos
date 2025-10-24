{$H+}   //String is an AnsiString
{$MODE OBJFPC}  //Enable Object Pascal

program main(output);

uses tcp_connection;

var
    a: integer;
    tcp_comm: TCPConnection;

begin
    a:= 1;
//    writeln('Connection exit code: ', tcp_comm.connect);
    a:= tcp_comm.connect;
//    tcp_comm.close;

end.
