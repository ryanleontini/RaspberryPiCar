from gpiozero import DistanceSensor as DS
import time

class DistanceSensor:
  def __init__(self, trigger=20, echo=21):
    self.sensor = DS(echo=echo, trigger=trigger)

  def run(self):
    try:
      while True:
        distance = self.sensor.distance * 100 # distance in cm

        print(f"Distance: {distance:.1f} cm", end="\r")

        # if car gets too close to object

        """
        if distance < 5:
          print("Too close! Stopping")
          return 0
        """
        
        time.sleep(0.1)

    except KeyboardInterrupt:
      pass





