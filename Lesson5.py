import machine
import utime

LED = machine.Pin(16,machine.Pin.OUT)
BUTTON = machine.Pin(18,machine.Pin.IN)

while True:
    val = BUTTON.value()
    if val == 1:
        LED.value(1)
    else:
        LED.value(0)


