import RPi.GPIO as GPIO
import time
pin = 27

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)

GPIO.output(pin, 0)
