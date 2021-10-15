#!/usr/bin/python3
# -*- coding:UTF-8 -*-

import RPi.GPIO as GPIO
import time


###########################################################################
## Config #################################################################

# this is visually the relays, eg pin 16 is for the upper-right relay
RelayTop = [13, 19, 16]
RelayLow = [26, 20, 21]

# this is the index into array above of where the motors are wired
# you can invert the order (eg 2,1) to change polarity/direction of motors
MotorARelays = [1,2]
MotorBRelays = [4,5]

###########################################################################
###########################################################################

MotorAStateOff = [0,0]
MotorAStateFwd = [1,0]
MotorAStateRev = [0,1]

MotorBStateOff = [0,0]
MotorBStateFwd = [1,0]
MotorBStateRev = [0,1]

RelayChannels = [*RelayLow,*RelayTop]

# initial states
RelayStates = [0,0,0,0,0,0]
MotorADir = 0
MotorBDir = 0

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(RelayTop, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(RelayLow, GPIO.OUT, initial=GPIO.LOW)                              
time.sleep(1)


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
    #time.sleep(.005) #states take 5ms to apply 
  except:
    GPIO.cleanup()


def motors(adir, bdir):
  MotorADir = adir
  MotorBDir = bdir 

  if(adir == 0):
    RelayStates[MotorARelays[0]] = MotorAStateOff[0]
    RelayStates[MotorARelays[1]] = MotorAStateOff[1]
  if(adir == 1):
    RelayStates[MotorARelays[0]] = MotorAStateFwd[0]
    RelayStates[MotorARelays[1]] = MotorAStateFwd[1]
  if(adir == -1):
    RelayStates[MotorARelays[0]] = MotorAStateRev[0]
    RelayStates[MotorARelays[1]] = MotorAStateRev[1]

  if(bdir == 0):
    RelayStates[MotorBRelays[0]] = MotorBStateOff[0]
    RelayStates[MotorBRelays[1]] = MotorBStateOff[1]
  if(bdir == 1):
    RelayStates[MotorBRelays[0]] = MotorBStateFwd[0]
    RelayStates[MotorBRelays[1]] = MotorBStateFwd[1]
  if(bdir == -1):
    RelayStates[MotorBRelays[0]] = MotorBStateRev[0]
    RelayStates[MotorBRelays[1]] = MotorBStateRev[1]
  
  applyRelayStates()




motors(0,0)
time.sleep(1)

motors(1,0)
time.sleep(1)

motors(-1,0)
time.sleep(1)

motors(0,1)
time.sleep(1)

motors(0,-1)
time.sleep(1)

motors(1,1)
time.sleep(1)

motors(1,-1)
time.sleep(1)

motors(-1,1)
time.sleep(1)

motors(-1,-1)
time.sleep(1)

motors(0,0)
time.sleep(2)
