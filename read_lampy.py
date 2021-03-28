import RPi.GPIO as GPIO
import time
pin = 22

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)

while True:
	x = GPIO.input(pin)
	if x == 0:
		print("LAMPA SWIECI")
	else:
		print("LAMPA ZGASZONA")
	time.sleep(1)
