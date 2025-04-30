from gpiozero import DistanceSensor
import time

class Sensor:

  TRIGGER = 20
  ECHO = 21
  sensor;
  
  def _init_(self):
    self.sensor = DistanceSensor(echo=ECHO, trigger=TRIGGER)

  def run():
    try:
      while True:
        distance = sensor.distance
        time.sleep(0.1)
    except Keyboard Interrupt:
      pass





