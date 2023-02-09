import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
    while True:
        if GPIO.input(18) == 0:
           print('Wcisniety')

except KeyboardInterrupt:
    print('Koniec')

GPIO.cleanup()