#!/usr/bin/python3
# -*- coding:UTF-8 -*-

import RPi.GPIO as GPIO
import time

RelayLow = [21, 20, 26]
RelayTop = [16, 19, 13]



GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(RelayTop, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(RelayLow, GPIO.OUT, initial=GPIO.LOW)                              
time.sleep(2)
try:
  while True:
    print("turn on low")
    GPIO.output(RelayLow[0], GPIO.HIGH)
    time.sleep(1)
    
    print("turn off low")
    GPIO.output(RelayLow[0], GPIO.LOW)
    time.sleep(1)
    
    print("turn on top")
    GPIO.output(RelayTop[0], GPIO.HIGH)
    time.sleep(1)
    
    print("turn off top")
    GPIO.output(RelayTop[0], GPIO.LOW)
    time.sleep(3)

except:
  GPIO.cleanup()


