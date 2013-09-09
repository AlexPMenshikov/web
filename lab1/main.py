import socket

server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = 'localhost'
port = 8007
server_socket.bind((host,port))
server_socket.listen(3)
conn , addr = server_socket.accept()

print 'client is at', addr
#while 1:
data = conn.recv(1024)
c=conn.getpeername
print(c)
conn.send('HI 2 ALL')
conn.close()