#!/usr/bin/env python3

from mfrc522 import SimpleMFRC522
import RPi.GPIO as GPIO
import time

#Numery tagow RFID
BRELOK_1 = 85733152491
KARTA_1 = 219546064077
KARTA_2 = 704240555340 




def rfid_odczyt():
    reader = SimpleMFRC522()
    print("CZEKAM")
    try:
        id, text = reader.read()
        print("ODCZYT")
    finally:
        GPIO.cleanup()
    return id

def rfid_zapis(nazwa):
    reader = SimpleMFRC522()
    try:
        reader.write(nazwa)
        print("Przypisano")
    finally:
        GPIO.cleanup()

DRZWI_PIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(DRZWI_PIN, GPIO.OUT)
GPIO.output(DRZWI_PIN, 1)
while True:
	if rfid_odczyt() == BRELOK_1:
		print("DOSTEP")
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(DRZWI_PIN, GPIO.OUT)
		GPIO.output(DRZWI_PIN, 0)
		time.sleep(10)
		GPIO.output(DRZWI_PIN, 1)
			


