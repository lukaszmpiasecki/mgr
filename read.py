import RPi.GPIO as GPIO
import time
pin = 14

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
	x = GPIO.input(pin)
	print(x)
	time.sleep(1)
