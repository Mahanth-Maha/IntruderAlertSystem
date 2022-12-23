import RPi.GPIO as GPIO
import time

# Set up the GPIO pins for the PIR sensor
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN)

# Set up the LED
GPIO.setup(24, GPIO.OUT)

try:
    while True:
        # Check the PIR sensor
        if GPIO.input(18):
            # Turn on the LED
            GPIO.output(24, GPIO.HIGH)
            print("Motion detected!")
            time.sleep(1)
        else:
            # Turn off the LED
            GPIO.output(24, GPIO.LOW)
            time.sleep(0.1)

except KeyboardInterrupt:
    # Clean up the GPIO pins before exiting
    GPIO.cleanup()

# import RPi.GPIO as GPIO
# import time

# # Set up the GPIO pins for the PIR sensor
# GPIO.setmode(GPIO.BCM)
# GPIO.setup(18, GPIO.IN)
# GPIO.setup(24, GPIO.OUT)

# # Set up the ACT LED
# ACT_LED_PATH = "/sys/class/leds/led0/brightness"

# try:
#     while True:
#         # Check the PIR sensor
#         if GPIO.input(18):
#             # Turn on the ACT LED
#             with open(ACT_LED_PATH, "w") as f:
#                 f.write("1")
#             GPIO.output(24, GPIO.HIGH)
#             print("Motion detected!")
#             time.sleep(1)
#         else:
#             # Turn off the ACT LED
#             with open(ACT_LED_PATH, "w") as f:
#                 f.write("0")
#             GPIO.output(24, GPIO.LOW)
#             time.sleep(0.1)

# except KeyboardInterrupt:
#     # Clean up the GPIO pins before exiting
#     GPIO.cleanup()
