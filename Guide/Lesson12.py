'''from ws2812 import WS2812
import utime

black = (0,0,0)
red = (255,0,0)
yellow = (255,150,0)
green = (0,255,0)
cyan = (0,255,255)
blue = (0,0,255)
purple = (180,0,255)
white = (255,255,255)

colors = (black,red,yellow,green,cyan,blue,purple,white)

led = WS2812(18,1)

while True:
    print("fills")
    for color in colors:
        led.pixels_fill(color)
        led.pixels_show()
        utime.sleep(0.2)
'''

from ws2812 import WS2812
from machine import I2C,Pin,ADC
from utime import sleep

led = WS2812(18,1)
light_sensor = ADC(0)
sound_sensor = ADC(1)

while True:
    average = 0

    light = light_sensor.read_u16()/256
    for i in range(1000):
        noise =sound_sensor.read_u16()/256
        average += noise
    noise = average/1000

    print("noise :" + str(noise))

    if light < 80 :
        led.pixels_fill((255,255,255))
        led.pixels_show()
        sleep(0.1)
    else:
        if noise < 25:
            led.pixels_fill((0,255,0))
            led.pixels_show()
            sleep(1)
        elif noise >=25 and noise < 50:
            led.pixels_fill((255,255,0))
            led.pixels_show()
            sleep(1)
        elif noise >= 50:
            led.pixels_fill((255,0,0))
            led.pixels_show()
            sleep(1)
