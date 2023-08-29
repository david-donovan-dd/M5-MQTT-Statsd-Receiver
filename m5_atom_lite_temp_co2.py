from m5stack import *
from m5ui import *
from uiflow import *
from m5mqtt import M5mqtt
import time
import unit

co2_0 = unit.get(unit.CO2_SCD40, unit.PORTA)

periodic = None
room = None
temp = None
co2 = None

periodic = 0
co2_0.self_test()
rgb.setColorAll(0xcc33cc)
m5mqtt = M5mqtt('', 'm5server.local', 1883, '', '', 300)
m5mqtt.start()
room = ' office'
co2_0.wake_up()
co2_0.start_periodic_measurement()
wait(5)
while True:
  rgb.setColorAll(0x33ff33)
  co2_0.read_sensor_measurement()
  temp = co2_0.temperature
  temp = temp * 1.8
  temp = temp + 32
  temp = str(temp)
  temp = temp + room
  m5mqtt.publish(str('temp'), str(temp), 0)
  co2 = co2_0.co2
  co2 = str(co2)
  co2 = co2 + room
  m5mqtt.publish(str('co2'), str(co2), 0)
  wait(10)
