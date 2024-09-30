from lcd1602 import LCD1602
from dht11 import *
from machine import PWM, I2C, ADC, Pin
from utime import sleep_ms, sleep
import _thread

i2c = I2C(1, scl=Pin(7), sda=Pin(6), freq=400000)
d = LCD1602(i2c, 2, 16)
d.display()

dht = DHT(18)

buzzer = PWM(Pin(16))
LED = PWM(Pin(20))

Pot = ADC(0) #Max 65535 Min 352

temp_consigne = 0
temp_actu = 0
running = True
a = 0.003068

def ConversionTemp(x):
    return a*x+15

def VerifTemp():
    global temp_consigne

    temp_actu = dht.readTemperature()
    if temp_actu > temp_consigne:
        LED.duty_u16(65535)
        while temp_actu > temp_consigne + 3:
            buzzer.freq(1000)
            buzzer.duty_u16(1000)
            d.clear()
            d.print("ALARM")
            temp_consigne = ConversionTemp(Pot.read_u16())
            sleep_ms(250)
        buzzer.duty_u16(0)
    else:
        LED.duty_u16(0)

    sleep(1)

_thread.start_new_thread(VerifTemp(), ())

try:
    while running:
        d.clear()
        d.setCursor(0,0)
        d.print("Set : " + str(temp_consigne))
        d.print("Ambient")
        temp_consigne = ConversionTemp(Pot.read_u16())
        sleep(1)

except KeyboardInterrupt:
    print("Program stopped")

finally:
    running = False
    sleep(0.5)