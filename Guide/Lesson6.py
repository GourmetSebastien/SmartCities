from machine import ADC,Pin
from utime import sleep

ROTARY_ANGLE_SENSOR = ADC(0)
LED = Pin(16,Pin.OUT)

while True:
    print(ROTARY_ANGLE_SENSOR.read_u16())
    if ROTARY_ANGLE_SENSOR.read_u16() > 20000 and ROTARY_ANGLE_SENSOR.read_u16() < 40000:
        LED.value(1)
        sleep(1)
    else:
        LED.value(0)
        sleep(1)