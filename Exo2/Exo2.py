from machine import Pin, PWM, ADC
from time import sleep
import _thread

buzzer = PWM(Pin(27))
sensor = ADC(0)

vol = 1000
running = True

def volume():
    global running, vol

    while running:
        vol = sensor.read_u16()
        buzzer.duty_u16(vol)
        sleep(0.1)


#region Note musique
def DO(tmp):
    buzzer.freq(523)  # C4
    buzzer.duty_u16(vol)
    sleep(tmp)

def RE(tmp):
    buzzer.freq(587)  # D4
    buzzer.duty_u16(vol)
    sleep(tmp)

def MI(tmp):
    buzzer.freq(659)  # E4
    buzzer.duty_u16(vol)
    sleep(tmp)

def FA(tmp):
    buzzer.freq(698)  # F4
    buzzer.duty_u16(vol)
    sleep(tmp)

def SO(tmp):
    buzzer.freq(784)  # G4
    buzzer.duty_u16(vol)
    sleep(tmp)

def LA(tmp):
    buzzer.freq(880)  # A4
    buzzer.duty_u16(vol)
    sleep(tmp)

def SI(tmp):
    buzzer.freq(988)  # B4
    buzzer.duty_u16(vol)
    sleep(tmp)

def DOH(tmp):  # C5
    buzzer.freq(1046)
    buzzer.duty_u16(vol)
    sleep(tmp)

def N(tmp):  
    buzzer.duty_u16(0)
    sleep(tmp)

#endregion

#region Musique
def Tetris():
    DO(0.4)
    SO(0.4)
    LA(0.4)
    DOH(0.4)
    LA(0.4)
    SO(0.4)
    N(0.4)

    DO(0.4)
    SO(0.4)
    LA(0.4)
    DOH(0.4)
    LA(0.4)
    SO(0.4)
    N(0.4)

    DO(0.4)
    RE(0.4)
    MI(0.4)
    FA(0.4)
    MI(0.4)
    RE(0.4)
    N(0.4)

    DO(0.4)
    RE(0.4)
    MI(0.4)
    FA(0.4)
    MI(0.4)
    RE(0.4)
    N(0.4)

    N(0.5)
#endregion

_thread.start_new_thread(volume,())

try:
    while running:  
        Tetris()

except KeyboardInterrupt:
    print("Program stopped")

finally:
    running = False
    sleep(0.5)


