import time
from motor_driver import MotorDriver
from distance_sensor import DistanceSensor
from led_indicator import LEDIndicator

def main():
    try:
        # Initialize each component

        #GPIO6, GPIO13, GPIO19, GPIO26
        motor = MotorDriver(in1=6, in2=13, in3=19, in4=26)

        motor.stop()
        
        while True:
            
            # Distance sensor code
            distance_sensor = DistanceSensor()
            distance_sensor.run()

            # LED code

    except KeyboardInterrupt:
        # Control direction

    finally:
        # Clean up

if __name__ == "__main__":
    main()
