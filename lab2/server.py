import socket
import os

server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = '127.0.0.1'
port = 8000
path="C:/"
server_socket.bind((host,port))
server_socket.listen(1)
conn , addr = server_socket.accept()
data = os.listdir(path)+"\n"+conn.recv(1024)
conn.send(data)
#conn.sendall(data)
#print(os.getcwd())
conn.close()