import machine
import utime
from lcd1602 import LCD1602
import dht11

i2c = machine.I2C(1,scl= machine.Pin(7), sda=machine.Pin(6), freq=400000)
d = LCD1602(i2c, 2, 16)
d.display()
dht2 = dht11.DHT(16)
fan = machine.Pin(18,machine.Pin.OUT)

while True:
    temp = dht2.readTemperature()
    utime.sleep(0.25)
    d.clear()
    d.setCursor(0,0)
    d.print("Temp " + str(temp))
    utime.sleep(1)
    if temp > 22:
        fan.value(1)
    else:
        fan.value(0)