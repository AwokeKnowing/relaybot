#!/usr/bin/python3
# -*- coding:UTF-8 -*-

# by AwokeKnowing

import RPi.GPIO as GPIO


###########################################################################
## Config #################################################################

# this is visually the relays, eg pin 16 is for the upper-right relay
RelayChannels = [13, 19, 16,
                 26, 20, 21]

# this is the index into RelayChannels array 
# you can invert the order (eg 2,1) to change polarity/direction of motors
MotorLRelays = [5,4]
MotorRRelays = [2,1]

###########################################################################
###########################################################################


# activation pattern of MotorRelays corresponding to direction
# ie it requires 2 relays per direction
MotorStateOff = [0,0]
MotorStateFwd = [1,0]
MotorStateRev = [0,1]

# initial states
RelayStates = [0,0,0,0,0,0]  # 1 for high 0 for low
MotorLDir = 0                # current state of motor
MotorRDir = 0                # dir can be on of: -1 0 1 

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(RelayChannels, GPIO.OUT, initial=GPIO.LOW)


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
    # fyi states take 5ms to apply (time.sleep(.005))
  except:
    GPIO.cleanup()
    return False

  return True


def motors(left, right):
  MotorLDir = left
  MotorRDir = right 

  if(left == 0):
    RelayStates[MotorLRelays[0]] = MotorStateOff[0]
    RelayStates[MotorLRelays[1]] = MotorStateOff[1]
  if(left == 1):
    RelayStates[MotorLRelays[0]] = MotorStateFwd[0]
    RelayStates[MotorLRelays[1]] = MotorStateFwd[1]
  if(left == -1):
    RelayStates[MotorLRelays[0]] = MotorStateRev[0]
    RelayStates[MotorLRelays[1]] = MotorStateRev[1]

  if(right == 0):
    RelayStates[MotorRRelays[0]] = MotorStateOff[0]
    RelayStates[MotorRRelays[1]] = MotorStateOff[1]
  if(right == 1):
    RelayStates[MotorRRelays[0]] = MotorStateFwd[0]
    RelayStates[MotorRRelays[1]] = MotorStateFwd[1]
  if(right == -1):
    RelayStates[MotorRRelays[0]] = MotorStateRev[0]
    RelayStates[MotorRRelays[1]] = MotorStateRev[1]
  
  applyRelayStates()

