from machine import Pin, PWM
from time import sleep

buzzer = PWM(Pin(27))
vol = 1000

# Définitions des notes (avec fréquence en Hz)
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

# Mélodie du thème de Tetris
while True:
    # Première partie
    DO(0.4)
    SO(0.4)
    LA(0.4)
    DOH(0.4)
    LA(0.4)
    SO(0.4)
    N(0.4)

    # Deuxième partie
    DO(0.4)
    SO(0.4)
    LA(0.4)
    DOH(0.4)
    LA(0.4)
    SO(0.4)
    N(0.4)

    # Troisième partie
    DO(0.4)
    RE(0.4)
    MI(0.4)
    FA(0.4)
    MI(0.4)
    RE(0.4)
    N(0.4)

    # Quatrième partie
    DO(0.4)
    RE(0.4)
    MI(0.4)
    FA(0.4)
    MI(0.4)
    RE(0.4)
    N(0.4)

    # Pause entre chaque cycle
    N(0.5)
