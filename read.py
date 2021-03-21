import RPi.GPIO as GPIO
import time
pin = 27

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)

while True:
	x = GPIO.input(pin)
	print(x)
	time.sleep(1)
