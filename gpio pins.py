import RPi.GPIO as GPIO
import time

# Define button pin mapping
BUTTON_PINS = {
    "start": 17,
    "back": 27,
    "left": 22,
    "right": 23
}

# Setup GPIO
GPIO.setmode(GPIO.BCM)

for pin in BUTTON_PINS.values():
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

print("Waiting for button presses. Press Ctrl+C to stop.")

try:
    while True:
        for name, pin in BUTTON_PINS.items():
            if GPIO.input(pin) == GPIO.LOW:
                print(f"{name.upper()} button pressed")
                time.sleep(0.2)  # debounce
except KeyboardInterrupt:
    print("Exiting program...")
finally:
    GPIO.cleanup()
