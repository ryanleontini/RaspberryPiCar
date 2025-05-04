import RPi.GPIO as GPIO
import time

class DistanceSensor:
  def __init__(self, trigger=20, echo=21):
    GPIO.setup(trigger, GPIO.OUT)
    GPIO.setup(echo, GPIO.IN)
    GPIO.output(trigger, False)

  def run(self):
    try:
      while True:
        GPIO.output(self.trigger, True)
        time.sleep(0.00001)
        GPIO.output(self.trigger, False)

        while GPIO.input(self.echo) == 0:
          start_time = time.time()

        while GPIO.input(self.echo) == 0:
          end_time = time.time()

        distance = (end_time - start_time) * 100

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





