import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.board)

TRIGGER = 20
ECHO = 21

GPIO.setup(TRIGGER, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
GPIO.output(TRIGGER, False)



