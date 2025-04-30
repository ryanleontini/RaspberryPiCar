from gpiozero import DistanceSensor
import time

TRIGGER = 20
ECHO = 21

sensor = DistanceSensor(echo=ECHO, trigger=TRIGGER)

try:
  while True:
    distance = sensor.distance
    time.sleep(0.1)
except Keyboard Interrupt:
  pass





