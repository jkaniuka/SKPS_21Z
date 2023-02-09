import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
GPIO.setwarnings(False)
p = GPIO.PWM(18, 1000) 
p.start(0)
for i in range(5):
        for dc in range(1, 100, 1):
                p.start(0)
                p.ChangeFrequency(dc*10)
                p.ChangeDutyCycle(dc)
                time.sleep(0.01)
                p.stop()
        for dc in range(100, 1, -1):
                p.start(0)
                p.ChangeFrequency(dc*10)
                p.ChangeDutyCycle(dc)
                time.sleep(0.01)
                p.stop()
#p.stop()
GPIO.cleanup()
