import RPi.GPIO as GPIO
import time

# Each function will run until it encounter a motor.stop() or another motor function

class MotorDriver:
    def __init__(self, in1, in2, in3, in4, ena=23, enb=24):
        # Motor A
        self.in1 = in1
        self.in2 = in2
        # Motor B
        self.in3 = in3
        self.in4 = in4
        self.ena = ena
        self.enb = enb

        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)

        GPIO.setup(self.in1, GPIO.OUT)
        GPIO.setup(self.in2, GPIO.OUT)
        GPIO.setup(self.in3, GPIO.OUT)
        GPIO.setup(self.in4, GPIO.OUT)
        GPIO.setup(self.ena, GPIO.OUT)
        GPIO.setup(self.enb, GPIO.OUT)

        self.pwm_a = GPIO.PWM(self.ena, 1000)  # 1 kHz frequency
        self.pwm_b = GPIO.PWM(self.enb, 1000)

        self.pwm_a.start(100)  # Default to 100% speed
        self.pwm_b.start(100)

    def set_speed(self, speed_percent):
        speed = max(0, min(100, speed_percent))  # Clamp between 0-100
        self.pwm_a.ChangeDutyCycle(speed)
        self.pwm_b.ChangeDutyCycle(speed)

    def forward(self):
        GPIO.output(self.in1, GPIO.HIGH)
        GPIO.output(self.in2, GPIO.LOW)
        GPIO.output(self.in3, GPIO.HIGH)
        GPIO.output(self.in4, GPIO.LOW)

    def backward(self):
        GPIO.output(self.in1, GPIO.LOW)
        GPIO.output(self.in2, GPIO.HIGH)
        GPIO.output(self.in3, GPIO.LOW)
        GPIO.output(self.in4, GPIO.HIGH)

    def stop(self):
        GPIO.output(self.in1, GPIO.LOW)
        GPIO.output(self.in2, GPIO.LOW)
        GPIO.output(self.in3, GPIO.LOW)
        GPIO.output(self.in4, GPIO.LOW)

    def left(self):
        GPIO.output(self.in4, GPIO.LOW)
        GPIO.output(self.in3, GPIO.HIGH)

        GPIO.output(self.in2, GPIO.LOW)
        GPIO.output(self.in1, GPIO.LOW)

    def right(self):
        GPIO.output(self.in1, GPIO.HIGH)
        GPIO.output(self.in2, GPIO.LOW)

        GPIO.output(self.in3, GPIO.LOW)
        GPIO.output(self.in4, GPIO.LOW)      

    def cleanup(self):
        self.pwm_a.stop()
        self.pwm_b.stop()
        GPIO.cleanup()
