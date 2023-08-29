from m5stack import *
from m5ui import *
from uiflow import *
from m5mqtt import M5mqtt
import time
import unit

env3_0 = unit.get(unit.ENV3, unit.PORTA)

room = None
temp = None

rgb.setColorAll(0xcc33cc)
m5mqtt = M5mqtt('', 'm5server.local', 1883, '', '', 300)
m5mqtt.start()
room = ' dining_room'
wait(5)
while True:
  rgb.setColorAll(0x33ff33)
  temp = env3_0.temperature
  temp = temp * 1.8
  temp = temp + 32
  temp = str(temp)
  temp = temp + room
  m5mqtt.publish(str('temp'), str(temp), 0)
  wait(10)
