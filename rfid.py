#!/usr/bin/env python3

from mfrc522 import SimpleMFRC522
import RPi.GPIO as GPIO
import time

#Numery tagow RFID
BRELOK_1 = 85733152491
KARTA_1 = 219546064077
KARTA_2 = 704240555340 
uprawnieni = {85733152491,219546064077,704240555340}
obecni = {}

def rfid_odczyt():
    reader = SimpleMFRC522()
    try:
        id, text = reader.read()
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
LAMPY_PIN = 22
GPIO.setmode(GPIO.BCM)
GPIO.setup(DRZWI_PIN, GPIO.OUT)
GPIO.output(DRZWI_PIN, 1)
GPIO.setup(LAMPY_PIN, GPIO.OUT)
GPIO.output(LAMPY_PIN, 1)

while True:
	if rfid_odczyt() in uprawnieni:
		if rfid_odczyt() in obecni:
			del obecni[rfid_odczyt()]
		else:
			obecni[rfid_odczyt()] = [rfid_odczyt()]
		if len(obecni) > 0:
			GPIO.setmode(GPIO.BCM)
			GPIO.setup(LAMPY_PIN, GPIO.OUT)
			GPIO.output(LAMPY_PIN, 0)
		else:
			GPIO.setmode(GPIO.BCM)
			GPIO.setup(LAMPY_PIN, GPIO.OUT)
			GPIO.output(LAMPY_PIN, 1)
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(DRZWI_PIN, GPIO.OUT)
		GPIO.output(DRZWI_PIN, 0)
		time.sleep(10)
		GPIO.output(DRZWI_PIN, 1)
			


