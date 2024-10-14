from machine import Pin, ADC, PWM
import utime

Potentimetre = ADC(0)
LED_PWM = PWM(Pin(18))

LED_PWM.freq(500)

'''
while True:
    val = Potentimetre.read_u16()
    LED_PWM.duty_u16(val)'''

val = 0

while True:
    while val<65535:
        val += 50
        utime.sleep_ms(1)
        LED_PWM.duty_u16(val)
    
    while val > 0:
        val -= 50
        utime.sleep_ms(1)
        LED_PWM.duty_u16(val)