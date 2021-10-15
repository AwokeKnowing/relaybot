#!/usr/bin/python3
# -*- coding:UTF-8 -*-

import time
import keyboard
from relaymotors import motors 

while not keyboard.is_pressed('esc'):
  if keyboard.is_pressed('up arrow'):
    motors(1,1)
    time.sleep(1)
    motors(0,0)

  if keyboard.is_pressed('down arrow'):
    motors(-1,-1)
    time.sleep(1)
    motors(0,0)

time.sleep(1)

#motors(1,0)
#time.sleep(1)

#motors(-1,0)
#time.sleep(1)

#motors(0,1)
#time.sleep(1)

#motors(0,-1)
#time.sleep(1)

#motors(1,1)
#time.sleep(1)

#motors(-1,-1)
#time.sleep(1)

#motors(-1,1)
#time.sleep(1)

#motors(1,-1)
#time.sleep(1)

#motors(0,0)
#time.sleep(2)
