import time
import requests
import adafruit_dht
import board

# Initialize DHT22 sensor (note the change from DHT11 to DHT22)
dht_device = adafruit_dht.DHT22(board.D4)

def read_temp():
    # Read temperature and humidity from the DHT22 sensor
    temp = dht_device.temperature
    hum = dht_device.humidity

    # Prepare the payload with temperature and humidity
    payload = {'temperature': temp, 'humidity': hum}
    return payload

while True:
    try:
        # Post the temperature and humidity to Ubidots
        #Edit raspberry with your devise label! And "TOKEN_HERE!!!", with your ubidots token!
        r = requests.post('http://things.ubidots.com/api/v1.6/devices/raspberry/?token=TOKEN_HERE!!!', data=read_temp())
        print('Posting temperatures to Ubidots')
        print(read_temp())
    except Exception as e:
        # Print the exception message for debugging purposes
        print(f"An error occurred: {e}")
        pass

    # Wait for 10 seconds before the next reading
    time.sleep(10)


