from gpiozero import RGBLED
import time

led = RGBLED (22, 27, 17)
for r in range(2):
        for g in range(2):
                for b in range(2):
                        led.color = (r, g, b)
                        time.sleep(0.5)