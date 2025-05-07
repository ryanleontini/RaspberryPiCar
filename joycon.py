import threading
from evdev import InputDevice, ecodes

# Path to the input device (change if needed)
JOYCON_INPUT_PATH = "/dev/input/event2"

# Deadzone for analog joystick drift
JOYSTICK_DEADZONE_RAW = 8000  # For ABS_RX / ABS_RY

# Normalize value from a raw range (used for legacy ABS_Y case)
def normalize(value, min_val=0, max_val=255):
    return round((2 * (value - min_val) / (max_val - min_val)) - 1, 2)

def joycon_control_loop(motor, device_path=JOYCON_INPUT_PATH):
    """Control loop to move the car based on joystick Y-axis input"""
    try:
        device = InputDevice(device_path)
        print(f"[Joy-Con] Connected to: {device.name}")
    except FileNotFoundError:
        print(f"[Joy-Con] ERROR: Could not find device at {device_path}")
        return

    rx = 0
    ry = 0

    for event in device.read_loop():
        if event.type == ecodes.EV_ABS:
            if event.code == ecodes.ABS_RX:
                rx = event.value
            elif event.code == ecodes.ABS_RY:
                ry = event.value

            # Determine action based on joystick direction
            if abs(rx) < JOYSTICK_DEADZONE_RAW and abs(ry) < JOYSTICK_DEADZONE_RAW:
                motor.stop()
                print("Stop     ", end="\r")
            elif abs(rx) > abs(ry):
                # Stronger horizontal movement → turn
                if rx < -JOYSTICK_DEADZONE_RAW:
                    motor.left()
                    print("Turn Left ", end="\r")
                elif rx > JOYSTICK_DEADZONE_RAW:
                    motor.right()
                    print("Turn Right", end="\r")
            else:
                # Stronger vertical movement → forward/backward
                if ry < -JOYSTICK_DEADZONE_RAW:
                    motor.forward()
                    print("Forward   ", end="\r")
                elif ry > JOYSTICK_DEADZONE_RAW:
                    motor.backward()
                    print("Backward  ", end="\r")

def start_joycon_control(motor, device_path=JOYCON_INPUT_PATH):
    """Start joystick control in a separate thread"""
    thread = threading.Thread(target=joycon_control_loop, args=(motor, device_path))
    thread.daemon = True
    thread.start()
