import RPi.GPIO as GPIO
import time
pin = 5

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.IN)

while True:
	x = GPIO.input(pin)
	print(x)
	time.sleep(1)
