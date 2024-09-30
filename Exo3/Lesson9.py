from lcd1602 import LCD1602
from machine import I2C, Pin, ADC, PWM
from utime import sleep

Potentiometre = ADC(0)
LED = PWM(Pin(18))
i2c = I2C(1,scl=Pin(7), sda=Pin(6), freq=400000)
LED.freq(500)
d= LCD1602(i2c, 2, 16)
d.display()

'''
d.display()
sleep(1)

d.clear()
d.print('Hello')

sleep(1)
d.setCursor(0, 1)
d.print('World')
'''
while True:
    val = Potentiometre.read_u16()
    LED.duty_u16(val)
    sleep(0.25)
    d.clear()
    d.setCursor(0, 0)
    d.print(str(Potentiometre.read_u16()))
    sleep(0.25)