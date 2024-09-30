from lcd1602 import LCD1602
from dht11 import *
from machine import PWM, I2C, ADC, Pin
from utime import sleep_ms, sleep
import _thread

i2c = I2C(1, scl=Pin(7), sda=Pin(6), freq=400000)
d = LCD1602(i2c, 2, 16)

dht = DHT(18)

buzzer = PWM(Pin(16))
LED = PWM(Pin(20))

Pot = ADC(0) #Max 65535 Min 352

temp_consigne = 0
current_temp = 0
running = True
a = 0.003068

def CalculPot(x):
    return a*x+15

def VerifTemp():
    global current_temp

    current_temp = dht.readTemperature()
    d.setCursor(0,1)
    d.print("Ambient :" + str(current_temp))

    if current_temp > temp_consigne:
        LED.freq(2000)
        LED.duty_u16(65535)
    else:
        LED.duty_u16(0)
    
    if current_temp + 3 > temp_consigne:
        buzzer.freq(1000)
        #buzzer.duty_u16(1000)
        d.clear()
        d.print("ALARM")
    else:
        buzzer.duty_u16(0)

    sleep(1)

_thread.start_new_thread(VerifTemp(), ())

try:
    while running:
        d.clear()
        d.setCursor(0,0)
        d.print("Set : " + str(temp_consigne))
        temp_consigne = Pot.read_u16()
        sleep(1)

except KeyboardInterrupt:
    print("Program stopped")

finally:
    running = False
    sleep(0.5)