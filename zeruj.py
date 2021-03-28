import RPi.GPIO as GPIO
import time
pin = 16

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)

GPIO.output(pin,0)
print("WYZEROWANY")
