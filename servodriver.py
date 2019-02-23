import RPi.GPIO as GPIO #Official GPIO package

# https://raspberrypi.stackexchange.com/questions/12966/what-is-the-difference-between-board-and-bcm-for-gpio-pin-numbering
# http://www.datasheetcafe.com/hs-55-datasheet-servo-motor/
# https://rpi.science.uoit.ca/lab/servo/

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
        print("Angle: " + str(angle))
        self.dutycycle = 100 * (self.zeropulsewidth + (angle * ((self.fullextensionpulsewidth - self.zeropulsewidth) / self.maxtravel))) / 20
        self.moveservo.start(self.dutycycle)
        print("MS: " + str(self.dutycycle * .2))
        print("Duty Cycle: " + str(self.dutycycle) + "%")
        print("----------------")
    def cleanup(self):
        GPIO.cleanup()