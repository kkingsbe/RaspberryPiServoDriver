import RPi.GPIO as GPIO #Official GPIO package

GPIO.setmode(GPIO.BCM)

class servo:
    def __init__(self, pin, zeropulsewidth, fullextensionpulsewidth, maxtravel):
        self.pin = pin
        self.zeropulsewidth = zeropulsewidth
        self.fullextensionpulsewidth = fullextensionpulsewidth
        self.maxtravel = maxtravel
        GPIO.setup(self.pin, GPIO.OUT)
        self.moveservo = GPIO.PWM(self.pin, 50)  # The servo is expecting a pulse every 20mms or 50hz
    def setangle(self, angle):
        #BROKEN
        # https://www.servocity.com/hitec-hs-55-servo
        print("Angle: " + str(angle))
        #self.dutycycle = 4.5 + ((float(angle) / 90) * 5)
        self.dutycycle = 100 * (self.zeropulsewidth + (angle * ((self.fullextensionpulsewidth - self.zeropulsewidth) / self.maxtravel))) / 20
        self.moveservo.start(self.dutycycle)
        print("MS: " + str(self.dutycycle * .2))
        print("Duty Cycle: " + str(self.dutycycle) + "%")
        print("----------------")
    def setdc(self, dc):
        self.dutycycle = float(dc / 20) * 100
        self.moveservo.start(self.dutycycle)
        #time.sleep(2)
        print("Duty Cycle: " + str(self.dutycycle))
    def cleanup(self):
        GPIO.cleanup()