import socket

server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = '127.0.0.1'
port = 8000
server_socket.bind((host,port))
server_socket.listen(1)
while 1:
    conn , addr = server_socket.accept()
    print 'client is at', addr
    data = conn.recv(1024)
    conn.send(data)
    break
conn.close()
