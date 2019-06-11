# client side

import socket 
from _socket import AF_INET

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host=socket.gethostname()
print("host",host)
port=9999
s.connect((host,port))
msg=s.recv(1024)
s.close()
print(msg.decode('ascii'))