import RPi.GPIO as GPIO
import time
pin = 22

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)

while True:
	x = GPIO.input(pin)
	print("LAMPY ", x)
	time.sleep(1)
