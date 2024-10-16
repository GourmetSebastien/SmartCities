from machine import Pin, PWM, ADC, Timer
from time import sleep
import _thread

buzzer = PWM(Pin(27))
sensor = ADC(0)

vol = 1000
running = True

#region Note musique
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

def DO5(tmp):
    buzzer.freq(2093)
    buzzer.duty_u16(vol)
    sleep(tmp)

def N(tmp):  
    buzzer.duty_u16(0)
    sleep(tmp)

#endregion

#region Musique
def Frere():
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
    
#endregion

def volume():
    global running, vol

    while running:
        vol = sensor.read_u16()
        buzzer.duty_u16(vol)
        sleep(0.1)
        
_thread.start_new_thread(volume,())

try:
    while running: 
        Frere()
        sleep(2)

except KeyboardInterrupt:
    print("Program stopped")

finally:
    running = False
    buzzer.duty_u16(0)
    sleep(0.5)

