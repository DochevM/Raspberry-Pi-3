import time
import board
import adafruit_dht
import adafruit_ssd1306
from PIL import Image, ImageDraw, ImageFont
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

# Initialize the DHT11 sensor
dht_device = adafruit_dht.DHT22(board.D24)  # Use the GPIO pin you connected to

# Initialize the SSD1306 display
DISPLAY_WIDTH = 128
DISPLAY_HEIGHT = 64
DISPLAY_ADDRESS = 0x3C  # Default I2C address for the SSD1306

# Set up I2C for the display
i2c = board.I2C()
display = adafruit_ssd1306.SSD1306_I2C(DISPLAY_WIDTH, DISPLAY_HEIGHT, i2c)

# Create an image object to draw on the display
image = Image.new('1', (DISPLAY_WIDTH, DISPLAY_HEIGHT))
draw = ImageDraw.Draw(image)

# Load a default font
font = ImageFont.load_default()

def display_readings(temperature, humidity):
    # Clear the display
    draw.rectangle((0, 0, DISPLAY_WIDTH, DISPLAY_HEIGHT), outline=0, fill=0)

    # Draw the temperature and humidity on the display
    draw.text((0, 0), f"Temp: {temperature:.1f}C", font=font, fill=255)
    draw.text((0, 20), f"Humidity: {humidity:.1f}%", font=font, fill=255)

   # Display the image
    display.image(image)
    display.show()

def update_leds(temperature_c):
    # Turn off all LEDs initially
    GPIO.output(RED_LED_PIN, GPIO.LOW)
    GPIO.output(GREEN_LED_PIN, GPIO.LOW)
    GPIO.output(BLUE_LED_PIN, GPIO.LOW)

    # Turn on the appropriate LED based on temperature
    if temperature_c >= 30:
        GPIO.output(RED_LED_PIN, GPIO.HIGH)
    elif 20 >= temperature_c <= 30:
        GPIO.output(GREEN_LED_PIN, GPIO.HIGH)
    else:
        GPIO.output(BLUE_LED_PIN, GPIO.HIGH)

while True:
    try:
        # Read temperature and humidity from the DHT11 sensor
        temperature_c = dht_device.temperature
        humidity = dht_device.humidity
        update_leds(temperature_c)

        if humidity is not None and temperature_c is not None:
            display_readings(temperature_c, humidity)
        else:
            print("Failed to retrieve data from sensor")

    except RuntimeError as error:
        print(f"RuntimeError: {error}")
        GPIO.output(RED_LED_PIN, GPIO.LOW)
        GPIO.output(GREEN_LED_PIN, GPIO.LOW)
        GPIO.output(BLUE_LED_PIN, GPIO.LOW)

    # Wait before the next reading
    time.sleep(2)



