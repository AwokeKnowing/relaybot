#!/usr/bin/python
# -*- coding:UTF-8 -*-

import RPi.GPIO as GPIO
import time

RelayTop = [21, 20, 26]
RelayLow = [16, 19, 13]



GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(RelayA, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(RelayB, GPIO.OUT, initial=GPIO.LOW)
time.sleep(2)
try:
  while True:
    print("turn on low")
    GPIO.output(RelayLow, GPIO.HIGH)
    time.sleep(1)
    
    print("turn off low")
    GPIO.output(RelayLow, GPIO.LOW)
    time.sleep(1)
    
    print("turn on top")
    GPIO.output(RelayTop, GPIO.HIGH)
    time.sleep(1)
    
    print("turn off top")
    GPIO.output(RelayTop, GPIO.LOW)
    time.sleep(3)

except:
  GPIO.cleanup()