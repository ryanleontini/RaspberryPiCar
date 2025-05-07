import time
import threading
from motor_driver import MotorDriver
from distance_sensor import DistanceSensor
from joycon import start_joycon_control

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
    motor.backward()
    time.sleep(1.0)
    motor.stop()

    # Turn around - 4 point turn
    motor.backward_left()
    time.sleep(0.1)
    motor.right()
    time.sleep(0.1)
    motor.backward_left()
    time.sleep(0.1)
    motor.right()
    motor.stop()

def main():
    motor = MotorDriver(in1=6, in2=13, in3=19, in4=26, ena=23, enb=24)
    # Set speed between 0 - 100
    motor.set_speed(40)
    start_joycon_control(motor)

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

    except KeyboardInterrupt:
        print("Interrupted by user")

    finally:
        stop_event.set()
        motor.cleanup()
        print("GPIO cleaned up")

if __name__ == "__main__":
    main()
