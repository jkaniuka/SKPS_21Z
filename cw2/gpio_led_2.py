import RPi.GPIO as GPIO
from time import sleep
import math

GPIO.setmode(GPIO.BCM)
green = 18
GPIO.setup(green, GPIO.OUT)
for i in range(10000):
        GPIO.output(green, GPIO.HIGH)
        sleep(0.001*abs(math.sin(i*0.001)))
        GPIO.output(green, GPIO.LOW)
        sleep(0.001*(1-abs(math.sin(i*0.001))))
