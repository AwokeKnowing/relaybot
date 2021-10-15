#!/usr/bin/python3
# -*- coding:UTF-8 -*-

import time
import curses
import asyncio
from relaymotors import motors 



def program(screen):

  curses.curs_set(0)
  screen.nodelay(True)

  while True:
    char = screen.getch()
    if char == 113: break  # q
    elif char == curses.KEY_RIGHT: 
      print("right")
      motors(1,-1)
      time.sleep(.1)
      
    elif char == curses.KEY_LEFT: 
      print("left")
      motors(-1,1)
      time.sleep(.1)
      
    elif char == curses.KEY_UP: 
      print("up")
      motors(1,1)
      time.sleep(.1)
      
    elif char == curses.KEY_DOWN: 
      print("down")
      motors(-1,-1)
      time.sleep(.1)

    else: 
      motors(0,0)
      time.sleep(.1)
      
    time.sleep(0.1)


curses.wrapper(program)

exit()
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
