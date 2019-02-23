import socket

TCP_IP = 'raspberrypiUAV'
TCP_PORT = 5005
BUFFER_SIZE = 1024
MESSAGE = b""

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
while MESSAGE != b"end":
    MESSAGE = bytes(input("Enter Message: "), 'utf-8') # Make sure utf-8 is specified
    s.send(MESSAGE)
    data = s.recv(BUFFER_SIZE)
s.close()

print("received data:", data)