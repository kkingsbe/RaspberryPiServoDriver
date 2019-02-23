import socket, servodriver

servo = servodriver.servo(14, .6, 2.4, 203)

TCP_IP = socket.gethostname()
TCP_PORT = 5005
BUFFER_SIZE = 20  # Normally 1024, but we want fast response

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', TCP_PORT))
s.listen(1)

conn1, addr = s.accept()
print('Connection address:', addr)
while 1:
    data = conn1.recv(BUFFER_SIZE)
    if not data or data == b"end": break
    print("received data:", data)
    conn1.send(b"Turning to " + data)  # echo
    servo.setangle(float(data))
conn1.close()
servo.cleanup()