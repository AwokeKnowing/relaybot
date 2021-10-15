#!/usr/bin/python3
# -*- coding:UTF-8 -*-

import RPi.GPIO as GPIO
import time

RelayLow = [21, 20, 26]
RelayTop = [16, 19, 13]

RelayChannels=[*RelayLow,*RelayTop]
RelayStates = [0,0,0,0,0,0]

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(RelayTop, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(RelayLow, GPIO.OUT, initial=GPIO.LOW)                              
time.sleep(2)


def getRelayStates():
  return RelayStates

def applyRelayStates():


  try:
    GPIO.output([RelayChannels[i] 
                  for i in range(6) if RelayStates[i]==0], 
                GPIO.LOW)
    GPIO.output([RelayChannels[i] 
                  for i in range(6) if RelayStates[i]==1], 
                GPIO.HIGH)
  except:
    GPIO.cleanup()



applyRelayStates()
time.sleep(2)
RelayStates=[1,0,1,0,1,0]
applyRelayStates()
time.sleep(2)
RelayStates=[0,1,0,1,0,1]
applyRelayStates()
time.sleep(2)
RelayStates=[0,0,0,0,0,0]
applyRelayStates()