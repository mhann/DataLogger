import socket
TCP_IP = 'raspberrypi'
TCP_PORT = 5005
BUFFER_SIZE = 1024
var = 0
MESSAGE = "Hello, World!"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.send(MESSAGE.encode())
s.send(str(var).encode())
data = s.recv(BUFFER_SIZE)
var = var + 1
s.close()
print("received data:", data.decode())
