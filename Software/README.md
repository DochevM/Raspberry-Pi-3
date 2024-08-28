
# Used Sensors and Libraries for Raspberry Pi 3

This README provides information about the libraries used with various sensors on a Raspberry Pi 3. The focus is on the DHT22 digital temperature and humidity sensor.

## DHT22 - Digital Temperature and Humidity Sensor
[DHT22](https://store.comet.bg/Catalogue/Product/50013/) (or AM2302) is a low-cost digital temperature and humidity sensor with better accuracy and a broader range than the DHT11.

### Libraries for DHT22
- [Adafruit_CircuitPython_DHT](https://github.com/adafruit/Adafruit_CircuitPython_DHT)  
  This library is used for interfacing with DHT sensors (like DHT11 and DHT22).

## L-154A4SUREQBFZGEW - LED
The [L-154A4SUREQBFZGEW](https://github.com/DochevM/Raspberry_Pi_3/blob/main/Documents/L-154A4SUREQBFZGEW.pdf) is a high-intensity RGB LED. While no specific library is required to control LEDs, you can use GPIO libraries to manage its operation.

### Libraries for GPIO Control
- [RPi.GPIO](https://pypi.org/project/RPi.GPIO/)  
  A Python library for controlling the GPIO pins on the Raspberry Pi, useful for handling digital outputs like LEDs.
- [gpiozero](https://gpiozero.readthedocs.io/en/stable/)  
  A Python library that provides a simple interface for controlling GPIO devices, including LEDs, switches, and more.

## WEA012864DWPP3N00003 - OLED Display
[WEA012864DWPP3N00003](https://store.comet.bg/Catalogue/Product/51127/) is a 0.96-inch COG OLED display with a resolution of 128x64 pixels.

### Libraries for WEA012864DWPP3N00003
- [Pillow](https://github.com/python-pillow/Pillow)  
  This library is used for image handling, necessary for drawing text and graphics on the
- [Adafruit_CircuitPython_SSD1306](https://github.com/adafruit/Adafruit_CircuitPython_SSD1306)  
  Used for controlling SSD1306 OLED displays.
