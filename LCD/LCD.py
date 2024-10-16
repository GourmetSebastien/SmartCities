from lcd1602 import LCD1602
from dht11 import *
from machine import PWM, I2C, ADC, Pin
from utime import sleep,sleep_ms

i2c = I2C(1, scl=Pin(7), sda=Pin(6), freq=400000)
d = LCD1602(i2c, 2, 16)
d.display()

dht = DHT(18)

buzzer = PWM(Pin(16))
LED_PWM = PWM(Pin(20))
LED_PWM.freq(500)

Pot = ADC(0) #Max 65535 Min 352

temp_consigne = 0
temp_actu = 0
a = 0.0003068
running = True

def ConversionTemp(x):
    return a*x+15

while running:
    temp_consigne = ConversionTemp(Pot.read_u16())

    temp_actu = dht.readTemperature()
    if temp_actu > temp_consigne:
        LED_PWM.duty_u16(65535)
        while temp_actu > temp_consigne + 3:
            buzzer.freq(1000)
            buzzer.duty_u16(1000)
            d.clear()
            d.print("ALARM")
            temp_consigne = ConversionTemp(Pot.read_u16())
            sleep_ms(250)
        buzzer.duty_u16(0)
    else:
        LED_PWM.duty_u16(0)
        
    d.clear()
    d.print("Set :" + str(temp_consigne))
    d.setCursor(0,1)
    d.print("Ambient : " + str(temp_actu))

    sleep(1)

