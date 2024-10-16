from machine import Pin
import utime
import _thread 

led = Pin(18, Pin.OUT)  
button = Pin(16, Pin.IN, Pin.PULL_DOWN) 

state = 0  
debounce_time = 0.2 
running = True 


state_lock = _thread.allocate_lock()

def monitor_button():
    global state, running
    last_button_state = 0 

    while running:
        current_button_state = button.value()

        if current_button_state == 1 and last_button_state == 0: 
            with state_lock:  
                state += 1
                if state > 3:  
                    state = 1
            utime.sleep(debounce_time)
        
        last_button_state = current_button_state
        utime.sleep(0.01) 

_thread.start_new_thread(monitor_button, ())

def toggle_led(state):
    if state == 1:
        return 1 
    elif state == 2:
        return 0.25 
    else:
        return None 

try:
    while running:
        with state_lock: 
            delay = toggle_led(state)

        if delay is not None: 
            led.toggle() 
            utime.sleep(delay) 
        else:
            led.value(0) 

except KeyboardInterrupt:
    print("Program stopped")
    led.value(0)

finally:
    running = False
    utime.sleep(0.5)
