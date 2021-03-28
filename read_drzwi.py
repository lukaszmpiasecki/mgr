import RPi.GPIO as GPIO
import time
pin = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.IN)

while True:
	x = GPIO.input(pin)
	if x == 0:
		print("DRZWI OTWARTE")
	else:
		print("DRZWI ZAMKNIETE")
	time.sleep(1)
