from gpiozero import DistanceSensor as ds
import time

class DistanceSensor:

  TRIGGER = 20
  ECHO = 21
  sensor;
  
  def _init_(self):
    self.sensor = ds(echo=ECHO, trigger=TRIGGER)

  def run():
    try:
      while True:
        distance = sensor.distance
        time.sleep(0.1)
    except Keyboard Interrupt:
      pass





