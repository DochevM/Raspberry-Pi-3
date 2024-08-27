import time
import adafruit_dht
import board
import RPi.GPIO as GPIO

# Setup GPIO
GPIO.setmode(GPIO.BCM)

# Define the GPIO pins for the LEDs
RED_LED_PIN = 22
GREEN_LED_PIN = 27
BLUE_LED_PIN = 17

# Setup the GPIO pins as outputs
GPIO.setup(RED_LED_PIN, GPIO.OUT)
GPIO.setup(GREEN_LED_PIN, GPIO.OUT)
GPIO.setup(BLUE_LED_PIN, GPIO.OUT)

# Initialize the DHT22 device
dht_device = adafruit_dht.DHT22(board.D24)

def update_leds(temperature):
    # Turn off all LEDs initially
    GPIO.output(RED_LED_PIN, GPIO.LOW)
    GPIO.output(GREEN_LED_PIN, GPIO.LOW)
    GPIO.output(BLUE_LED_PIN, GPIO.LOW)

    # Turn on the appropriate LED based on temperature
    if temperature >= 30:
        GPIO.output(RED_LED_PIN, GPIO.HIGH)
    elif 20 >= temperature <= 30:
        GPIO.output(GREEN_LED_PIN, GPIO.HIGH)
    else:
        GPIO.output(BLUE_LED_PIN, GPIO.HIGH)

while True:
    try:
        # Read temperature and humidity
        temperature_c = dht_device.temperature
        humidity = dht_device.humidity

        # Print the values to the console
        print("Temp:{:.1f} C    Humidity: {}%".format(temperature_c, humidity))

        # Update the LEDs based on temperature
        update_leds(temperature_c)

    except RuntimeError as err:
        # Handle errors
        print(err.args[0])
        GPIO.output(RED_LED_PIN, GPIO.LOW)
        GPIO.output(GREEN_LED_PIN, GPIO.LOW)
        GPIO.output(BLUE_LED_PIN, GPIO.LOW)


    # Wait before taking another reading
    time.sleep(2.0)

