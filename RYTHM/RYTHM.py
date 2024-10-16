from ws2812 import WS2812
from machine import ADC
from utime import sleep
import _thread
import random

#region color
black = (0, 0, 0)
red = (255, 0, 0)
yellow = (255, 150, 0)
green = (0, 255, 0)
cyan = (0, 255, 255)
blue = (0, 0, 255)
purple = (180, 0, 255)
white = (255, 255, 255)

colors = (black, red, yellow, green, cyan, blue, purple, white)
#endregion

led = WS2812(18, 1)
sound_sensor = ADC(1)

running = True
average = 0
old_average = 0
threshold = 1000

def sensor():
    global average
    while running:
        total_noise = 0
        for _ in range(50):
            noise = sound_sensor.read_u16()
            total_noise += noise
        average = total_noise / 50
        print(f"Averaged noise: {average:.2f}")
        sleep(0.1)

_thread.start_new_thread(sensor, ())

try:
    while running:
        print(f"Old Average: {old_average:.2f}, New Average: {average:.2f}")
        if average > old_average + threshold:
            new_color = random.choice(colors)
            led.pixels_fill(new_color)
            led.pixels_show()
            old_average = average 
            sleep(0.5)

        sleep(0.5)

except KeyboardInterrupt:
    print("Program stopped")

finally:
    running = False
    sleep(0.5)
