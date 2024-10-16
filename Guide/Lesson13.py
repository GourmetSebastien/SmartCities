from machine import Pin,PWM
from utime import sleep

'''servo = PWM(Pin(20))
servo.freq(100)

while True:
    servo.duty_u16(3050)
    sleep(1)
    servo.duty_u16(12750)
    sleep(1)'''

servo = PWM(Pin(20))
servo.freq(100)
Pir = Pin(18,Pin.IN)

while True:
    if Pir.value() == 1:
        print("Motion detected")
        servo.duty_u16(10500)
        sleep(10)

        servo.duty_u16(4500)