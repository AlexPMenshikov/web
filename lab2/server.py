import socket
import os

server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = socket.gethostbyname(socket.gethostname())
port = 8001
path="D:/"
server_socket.bind((host,port))
server_socket.listen(1)
while 1:
    conn , addr = server_socket.accept()
    print 'client is at', addr
    tmp = os.listdir(path)
    print(type(tmp))

    conn.recv(1024)
    data = ""
    print('len=',len(tmp))
    for x in tmp:
        data = data+x+"\n"
    #print(type(data))
    #print(data)
    break
conn.send(data)
conn.close()