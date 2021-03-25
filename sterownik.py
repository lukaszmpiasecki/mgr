#!/usr/bin/env python3

#Program na zaliczenie pracy magisterskiej

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import I2C_LCD_driver
import adafruit_dht as DHT
#import Adafruit_DHT as DHT
import board
import time
import sys
import datetime
#Numery tagow RFID
BRELOK_1 = 85733152491
KARTA_1 = 219546064077
KARTA_2 = 704240555340 
#PINY GPIO

DHT_PIN = 26
PIR_PIN = 16
HL83_PIN = 6
MQ2_PIN = 5
DRZWI_PIN = 17
ALARM_PIN = 27
LAMPY_PIN = 22

DHT_SENSOR = DHT.DHT11(DHT_PIN)

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR_PIN, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(HL83_PIN, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(MQ2_PIN, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(DRZWI_PIN, GPIO.OUT)
GPIO.output(DRZWI_PIN, 1)
GPIO.setup(ALARM_PIN, GPIO.OUT)
GPIO.output(ALARM_PIN, 1)
GPIO.setup(LAMPY_PIN, GPIO.OUT)
GPIO.output(LAMPY_PIN, 1)

def zalanie(pin):
    while GPIO.input(pin) == 0:
        mylcd.lcd_clear()
        mylcd.lcd_display_string("ALARM ZALANIE", 1, 0)
        GPIO.output(ALARM_PIN, 0)
        time.sleep(1)
        GPIO.output(ALARM_PIN, 1)
        time.sleep(1)

def zagazowanie(pin):
    while GPIO.input(pin) == 0:
        mylcd.lcd_clear()
        mylcd.lcd_display_string("ALARM", 1, 0)
        mylcd.lcd_display_string("DETEKCJA GAZU", 2, 0)
        GPIO.output(ALARM_PIN, 0)
        time.sleep(1)
        GPIO.output(ALARM_PIN, 1)
        time.sleep(1)

GPIO.add_event_detect(HL83_PIN, GPIO.FALLING)
GPIO.add_event_callback(HL83_PIN, zalanie)
GPIO.add_event_detect(MQ2_PIN, GPIO.FALLING)
GPIO.add_event_callback(MQ2_PIN, zagazowanie)

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

mylcd = I2C_LCD_driver.lcd()

while True:
    mylcd.lcd_clear()
    mylcd.lcd_display_string("TEMPERATURA %d%sC" % (DHT_SENSOR.temperature, chr(223)), 1, 0)
    mylcd.lcd_display_string("WILGOTNOSC %d%%" % (DHT_SENSOR.humidity), 2, 0)
    time.sleep(5)
    mylcd.lcd_clear()
    now = datetime.datetime.now()
    d = now.strftime("%Y-%m-%d")
    t = now.strftime("%H:%M")
    mylcd.lcd_display_string(d, 1, 0)
    mylcd.lcd_display_string(t, 2, 0)
    time.sleep(5)
