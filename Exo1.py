from machine import Pin
from time import sleep

led = Pin(16, Pin.OUT)
button = Pin(18, Pin.IN, Pin.PULL_DOWN)

state = 0
last_button_state = 0
debounce_time = 0.2

def toggle_led(state):
    if state == 1:
        return 1 
    elif state == 2:
        return 0.25
    else:
        return None

# Fonction principale
while True:
    current_button_state = button.value()

    if current_button_state == 1 and last_button_state == 0:
        state += 1
        if state > 3:
            state = 1
        sleep(debounce_time)

    last_button_state = current_button_state

    delay = toggle_led(state)

    if delay is not None: 
        led.toggle()
        sleep(delay)
    else:
        led.value(0)
