import RPi.GPIO as GPIO
import time, sys
GPIO.setmode(GPIO.BCM)
GPIO.setup(6, GPIO.IN)
def action(pin):
	if GPIO.input(6) == 0:
		print("WODA")
		print(GPIO.input(6))

GPIO.add_event_detect(6, GPIO.FALLING)
GPIO.add_event_callback(6, action)

while True:
	print("sprawdzam")
	print(GPIO.input(6))
	time.sleep(3)
