import threading
from evdev import InputDevice, ecodes

# Path to the input device (change if needed)
JOYCON_INPUT_PATH = "/dev/input/event2"

# Deadzone for analog joystick drift
JOYSTICK_DEADZONE_RAW = 8000  # For ABS_RX / ABS_RY
NORMALIZED_DEADZONE = 0.2     # For ABS_Y normalized fallback (if used)

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

    for event in device.read_loop():
        if event.type == ecodes.EV_ABS:
            if event.code == ecodes.ABS_RY:
                ry = event.value
                if abs(ry) < JOYSTICK_DEADZONE_RAW:
                    motor.stop()
                    print("Stop     ", end="\r")
                elif ry < -JOYSTICK_DEADZONE_RAW:
                    motor.forward()
                    print("Forward  ", end="\r")
                elif ry > JOYSTICK_DEADZONE_RAW:
                    motor.backward()
                    print("Backward ", end="\r")

def test_joystick_input(device_path=JOYCON_INPUT_PATH):
    """Standalone joystick tester: prints direction based on RX/RY"""
    try:
        device = InputDevice(device_path)
        print(f"[TEST] Connected to: {device.name}")
    except FileNotFoundError:
        print(f"[TEST] Could not find device at {device_path}")
        return

    print("[TEST] Move joystick to test directions (Ctrl+C to quit)...")

    rx, ry = 0, 0

    for event in device.read_loop():
        if event.type == ecodes.EV_ABS:
            if event.code == ecodes.ABS_RX:
                rx = event.value
            elif event.code == ecodes.ABS_RY:
                ry = event.value

            direction = "Center"
            if abs(rx) < JOYSTICK_DEADZONE_RAW and ry < -JOYSTICK_DEADZONE_RAW:
                direction = "Up"
            elif abs(rx) < JOYSTICK_DEADZONE_RAW and ry > JOYSTICK_DEADZONE_RAW:
                direction = "Down"
            elif rx < -JOYSTICK_DEADZONE_RAW and abs(ry) < JOYSTICK_DEADZONE_RAW:
                direction = "Left"
            elif rx > JOYSTICK_DEADZONE_RAW and abs(ry) < JOYSTICK_DEADZONE_RAW:
                direction = "Right"
            elif rx < -JOYSTICK_DEADZONE_RAW and ry < -JOYSTICK_DEADZONE_RAW:
                direction = "Up-Left"
            elif rx > JOYSTICK_DEADZONE_RAW and ry < -JOYSTICK_DEADZONE_RAW:
                direction = "Up-Right"
            elif rx < -JOYSTICK_DEADZONE_RAW and ry > JOYSTICK_DEADZONE_RAW:
                direction = "Down-Left"
            elif rx > JOYSTICK_DEADZONE_RAW and ry > JOYSTICK_DEADZONE_RAW:
                direction = "Down-Right"

            print(f"Joystick: rx={rx}, ry={ry} → {direction}     ", end="\r")

def start_joycon_control(motor, device_path=JOYCON_INPUT_PATH):
    """Start joystick control in a separate thread"""
    thread = threading.Thread(target=joycon_control_loop, args=(motor, device_path))
    thread.daemon = True
    thread.start()
