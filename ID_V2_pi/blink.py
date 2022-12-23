import RPi.GPIO as GPIO
import time

# Set up the GPIO pin for the LED
GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.OUT)

# Set the LED to blink at a rate of 1 Hz (once per second)
blink_rate = 1

try:
    while True:
        # Turn on the LED
        GPIO.output(24, GPIO.HIGH)
        time.sleep(blink_rate / 2)

        # Turn off the LED
        GPIO.output(24, GPIO.LOW)
        time.sleep(blink_rate / 2)

except KeyboardInterrupt:
    # Clean up the GPIO pin before exiting
    GPIO.cleanup()
