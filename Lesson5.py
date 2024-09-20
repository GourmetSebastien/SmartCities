import machine
import utime

LED = machine.Pin(16,machine.Pin.OUT)
BUTTON = machine.Pin(18,machine.Pin.IN)

val = 0

while True:
    if BUTTON.value() == 1:
        val += 1
        utime.sleep(1)

    elif val == 2 :
        val = 0
        utime.sleep(1)
        
    LED.value(val)