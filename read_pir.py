from gpiozero import MotionSensor
import RPi.GPIO as GPIO
import time
pin =16
pir = MotionSensor(pin)

pir.wait_for_motion()
print("RUCH")
