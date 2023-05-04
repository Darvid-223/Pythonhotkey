import keyboard
import time

trigger = 'fk'
replacement = "Försäkringskassan"
buffer = ''

def on_key_press(key_event):
    global buffer
    buffer += key_event.name
    
    if buffer.endswith(trigger):
        for _ in range(len(trigger)):
            keyboard.press('backspace')  # Use 'keyboard.press' instead of 'keyboard.press_key'
            keyboard.release('backspace')
        keyboard.write(replacement)
        buffer = ""

        keyboard.write('Försäkringskassan', delay=0.01)  # Write 'Försäkringskassan'

keyboard.on_press(on_key_press)

while True:
    time.sleep(1)

