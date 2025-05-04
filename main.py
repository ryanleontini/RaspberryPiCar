import time
import threading
from motor_driver import MotorDriver
from distance_sensor import DistanceSensor

DISTANCE_THRESHOLD = 5

def distance_monitor(sensor, motor, stop_event, routine_triggered):
    while not stop_event.is_set():
        dist = sensor.run()
        print(f"Distance: {dist} cm", end="\r")
        if dist < DISTANCE_THRESHOLD and not routine_triggered.is_set():
            print("\n Obstacle detected. Stopping car.")
            motor.stop()
            routine_triggered.set()
        time.sleep(0.1)

def reverse_routine(motor):
    # IAN - YOUR ROUTINE HERE - Check motor_driver.py for functions
    print("Starting reverse routine.")

def main():
    motor = MotorDriver(in1=6, in2=13, in3=19, in4=26)

    sensor = DistanceSensor()

    stop_event = threading.Event()
    routine_triggered = threading.Event()

    thread = threading.Thread(target=distance_monitor, args=(sensor, motor, stop_event, routine_triggered))
    thread.daemon = True
    thread.start()
    
    print("Controls: w = forward | s = backward | x = stop | q = quit")

    try:
        while True:
            if routine_triggered.is_set():
                reverse_routine(motor)
                routine_triggered.clear()
                continue
            
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
        stop_event.set()
        motor.cleanup()
        print("GPIO cleaned up")

if __name__ == "__main__":
    main()
