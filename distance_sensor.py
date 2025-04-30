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

        # if car gets too close to object
        if distance < 2:
          return 0
        
        time.sleep(0.1)
    except Keyboard Interrupt:
      pass





