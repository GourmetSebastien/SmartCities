from machine import Pin, PWM
from time import sleep

buzzer = PWM(Pin(27))

vol = 1000

def DO(tmp):
   buzzer.freq(1046)
   buzzer.duty_u16(vol)
   sleep(tmp)

def RE(tmp):
   buzzer.freq(1175)
   buzzer.duty_u16(vol)
   sleep(tmp)

def MI(tmp):
   buzzer.freq(1318)
   buzzer.duty_u16(vol)
   sleep(tmp)

def FA(tmp):
   buzzer.freq(1397)
   buzzer.duty_u16(vol)
   sleep(tmp)

def SO(tmp):
   buzzer.freq(1568)
   buzzer.duty_u16(vol)
   sleep(tmp)

def LA(tmp):
   buzzer.freq(1760)
   buzzer.duty_u16(vol)
   sleep(tmp)

def SI(tmp):
   buzzer.freq(1967)
   buzzer.duty_u16(vol)
   sleep(tmp)

def N(tmp):
   buzzer.duty_u16(0)
   sleep(tmp)

def frere_jacque():
   DO(0.25)
   RE(0.25)
   MI(0.25)
   DO(0.25)
   N(0.01)

   DO(0.25)
   RE(0.25)
   MI(0.25)
   DO(0.25)

   MI(0.25)
   FA(0.25)
   SO(0.5)

   MI(0.25)
   FA(0.25)
   SO(0.5)
   N(0.01)

   SO(0.125)
   LA(0.125)
   SO(0.125)
   FA(0.125)
   MI(0.25)
   DO(0.25)

   SO(0.125)
   LA(0.125)
   SO(0.125)
   FA(0.125)
   MI(0.25)
   DO(0.25)

   RE(0.25)
   SO(0.25)
   DO(0.5)
   N(0.01)

   RE(0.25)
   SO(0.25)
   DO(0.5)

while True:
   frere_jacque()