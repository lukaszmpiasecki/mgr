#!/usr/bin/env python3

#Program na zaliczenie pracy magisterskiej

import RPi.GPIO as GPIO
import I2C_LCD_driver
import adafruit_dht as DHT
import board
import time
import sys
import datetime

#PINY GPIO

DHT_PIN = 26
PIR_PIN = 16
HL83_PIN = 6
MQ2_PIN = 5
KONTAKTRON_PIN = 24
DRZWI_PIN = 17
ALARM_PIN = 27
LAMPY_PIN = 22
BUTTON_PIN = 14

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR_PIN, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(HL83_PIN, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(MQ2_PIN, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(DRZWI_PIN, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(ALARM_PIN, GPIO.OUT)
GPIO.output(ALARM_PIN, 1)
GPIO.setup(KONTAKTRON_PIN, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down = GPIO.PUD_UP)

def zalanie(pin):
    while GPIO.input(pin) == 0:
        while GPIO.input(BUTTON_PIN) == 1:
            mylcd.lcd_clear()
            mylcd.lcd_display_string("ALARM ZALANIE", 1, 0)
            GPIO.output(ALARM_PIN, 0)
            time.sleep(1)
            GPIO.output(ALARM_PIN, 1)
            time.sleep(1)

def zagazowanie(pin):
    while GPIO.input(pin) == 0:
        while GPIO.input(BUTTON_PIN) == 1:
            mylcd.lcd_clear()
            mylcd.lcd_display_string("ALARM", 1, 0)
            mylcd.lcd_display_string("DETEKCJA GAZU", 2, 0)
            GPIO.output(ALARM_PIN, 0)
            time.sleep(1)
            GPIO.output(ALARM_PIN, 1)
            time.sleep(1)

def drzwi(pin):
    if GPIO.input(pin) == 1:
        if GPIO.input(DRZWI_PIN) == 1:
            while GPIO.input(BUTTON_PIN) == 1:
                mylcd.lcd_clear()
                mylcd.lcd_display_string("ALARM", 1, 0)
                mylcd.lcd_display_string("DRZWI SFORSOWANE", 2, 0)
                GPIO.output(ALARM_PIN, 0)
                time.sleep(1)
                GPIO.output(ALARM_PIN, 1)
                time.sleep(1)

def wlamanie(pin):
    h = 23
    if h < 6 or h > 21:
        while GPIO.input(BUTTON_PIN) == 1:
            mylcd.lcd_clear()
            mylcd.lcd_display_string("ALARM", 1, 0)
            mylcd.lcd_display_string("WLAMANIE", 2, 0)
            GPIO.output(ALARM_PIN, 0)
            time.sleep(1)
            GPIO.output(ALARM_PIN, 1)
            time.sleep(1)

GPIO.add_event_detect(HL83_PIN, GPIO.FALLING)
GPIO.add_event_callback(HL83_PIN, zalanie)
GPIO.add_event_detect(MQ2_PIN, GPIO.FALLING)
GPIO.add_event_callback(MQ2_PIN, zagazowanie)
GPIO.add_event_detect(KONTAKTRON_PIN, GPIO.RISING)
GPIO.add_event_callback(KONTAKTRON_PIN, drzwi)
GPIO.add_event_detect(PIR_PIN, GPIO.RISING)
GPIO.add_event_callback(PIR_PIN, wlamanie)

#DEFINICJA URZADZEN
DHT_SENSOR = DHT.DHT11(DHT_PIN)
mylcd = I2C_LCD_driver.lcd()

def main_loop():

    while True:
        mylcd.lcd_clear()
        try:
            temp = DHT_SENSOR.temperature
            hum = DHT_SENSOR.humidity
        except RuntimeError:
            continue
        mylcd.lcd_clear()
        mylcd.lcd_display_string("TEMPERATURA %d%sC" % (temp, chr(223)), 1, 0)
        mylcd.lcd_display_string("WILGOTNOSC %d%%" % (hum), 2, 0)
        mylcd.lcd_display_string("TEMPERATURA %d%sC" % (DHT_SENSOR.temperature, chr(223)), 1, 0)
        mylcd.lcd_display_string("WILGOTNOSC %d%%" % (DHT_SENSOR.humidity), 2, 0)
        time.sleep(10)
        mylcd.lcd_clear()
        now = datetime.datetime.now()
        d = now.strftime("%Y-%m-%d")
        t = now.strftime("%H:%M")
        mylcd.lcd_display_string(d, 1, 0)
        mylcd.lcd_display_string(t, 2, 0)
        time.sleep(10)
        mylcd.lcd_clear()
        
main_loop()
