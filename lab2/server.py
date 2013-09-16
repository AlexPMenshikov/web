import socket
import os

server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = '127.0.0.1'
port = 8000
path="D:/"
server_socket.bind((host,port))
server_socket.listen(1)
while 1:
    conn , addr = server_socket.accept()
    print 'client is at', addr
    tmp = os.listdir(path)
    #ltmp = len(tmp)
    data = ""
    for x in tmp:
        #data = data+x+"\n"
        conn.send(x+"\n")
    #data = conn.recv(1024)
    #print(data)
    #conn.send(data)
    break
conn.close()