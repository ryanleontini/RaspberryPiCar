import time
from motor_driver import MotorDriver
from distance_sensor import DistanceSensor

def main():
    motor = MotorDriver(in1=6, in2=13, in3=19, in4=26)

    sensor = DistanceSensor()
    sensor.run()
    
    '''
    print("Controls: w = forward | s = backward | x = stop | q = quit")

    try:
        while True:
            cmd = input("Enter command: ").lower()
            if cmd == "w":
                motor.forward()
                print("Moving forward")
            elif cmd == "s":
                motor.backward()
                print("Reversing")
            elif cmd == "x":
                motor.stop()
                print("Stopping")
            elif cmd == "q":
                print("Exiting...")
                break
            else:
                print("Unknown command")

    except KeyboardInterrupt:
        print("Interrupted by user")

    finally:
        motor.cleanup()
        print("GPIO cleaned up")

    '''

if __name__ == "__main__":
    main()
