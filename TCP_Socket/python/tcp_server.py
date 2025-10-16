# EXEMPLO SERVIDOR TCP PARA PYTHON

'''
Referências:
https://docs.python.org/3/library/socket.html
https://realpython.com/python-sockets/
'''

import socket
import time

servidor = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#AF_INET -> IP V4 Protocol
#SOCK_TREAM -> TCP
#SOCK_DGRAM -> UDP

servidor.bind(('0.0.0.0', 1300))  #Listen port localhost 1300
servidor.listen()


while True:
    conn, addr = servidor.accept()     #conn is a socket object
    with conn:
        data = conn.recv(1024)         #Receiver max 1024 bytes of buffer
        if not data:                   #If nothing is received close the socket
            conn.close()               #... but the listen port is active
            continue
        else:							#If any bytes was received
            conn.sendall(data)               #Return to the client
            print('Recebido dados: ', data)
            print('Conectado ao IP: ', addr)
            time.sleep(0.01)              #Delay 10ms
            conn.close()                #Stop communication
