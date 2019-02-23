import time, servodriver

servo1 = servodriver.servo(14, .615, 2.39, 203)
te = 0

start = time.time()
while te <= 5:
    te = time.time() - start
    servo1.setangle(0)

start = time.time()
while te <= 5:
    te = time.time() - start
    servo1.setangle(45)

start = time.time()
while te <= 5:
    te = time.time() - start
    servo1.setangle(90)

#servo1.testrange()
'''
for dc in range(615,2390):
    servo1.setdc(dc / 1000)
    time.sleep(.1)
'''
servo1.cleanup()