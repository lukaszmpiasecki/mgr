import RPi.GPIO as GPIO
import time
pin = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.IN)

while True:
	x = GPIO.input(pin)
	print("DRZWI ", x)
	time.sleep(1)
