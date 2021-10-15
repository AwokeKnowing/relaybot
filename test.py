#!/usr/bin/python3
# -*- coding:UTF-8 -*-

import time
from relaymotors import motors 

time.sleep(1)

#motors(1,0)
#time.sleep(1)

#motors(-1,0)
#time.sleep(1)

#motors(0,1)
#time.sleep(1)

#motors(0,-1)
#time.sleep(1)

motors(1,1)
time.sleep(1)

motors(-1,-1)
time.sleep(1)

motors(-1,1)
time.sleep(1)

motors(1,-1)
time.sleep(1)

motors(0,0)
time.sleep(2)
