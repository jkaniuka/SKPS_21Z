
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
green = 18
GPIO.setup(green, GPIO.OUT)
for i in range(10):
        GPIO.output(green, GPIO.HIGH)
        sleep(1)
        GPIO.output(green, GPIO.LOW)
        sleep(1)




