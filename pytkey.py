
from pynput import keyboard
import fcntl
import sys
import re

version = 1.2
# kommentera bort under test i vs code terminal för att inte radera texten under test
#lock_file = open(sys.argv[0], 'w')
#try:
#    fcntl.flock(lock_file, fcntl.LOCK_EX | fcntl.LOCK_NB)
#except IOError:
#    print("Another instance is already running, quitting.")
#    sys.exit(0)
# ps aux | grep python | grep -v grep

buffer = ""  
# Calls function när tangent trycks
def on_key_press(key_event):
    global buffer  
    try:
        # Checkar om buffer innehåller "fka" när mellanslag trycks 
        if key_event == keyboard.Key.space:
#Hotrings
            if buffer.lower() == "fka":
                controller = keyboard.Controller()
                # Ta bort buffertangenter och mellanrum
                for _ in range(len(buffer) + 1):
                    controller.press(keyboard.Key.backspace)
                    controller.release(keyboard.Key.backspace)

                controller.type("Försäkringskassan ")
                buffer = ""  

            if buffer.lower() == "hla":
                controller = keyboard.Controller()

                for _ in range(len(buffer) + 1):
                    controller.press(keyboard.Key.backspace)
                    controller.release(keyboard.Key.backspace)

                controller.type("Handläggningsassistent ")
                buffer = ""

            else:
                    buffer = ""

        # If the backspace key is pressed, remove the last character from the buffer
        elif key_event == keyboard.Key.backspace:
            buffer = buffer[:-1]
        # If a printable character key is pressed, add it to the buffer
        elif isinstance(key_event, keyboard.KeyCode) and key_event.char.isprintable():
            buffer += key_event.char.lower()
    except Exception as e:
        print(f"Error occurred: {e}")
        buffer = ""  # Reset the buffer to prevent any further issues
# Start the listener to detect key presses and call the on_key_press function
with keyboard.Listener(on_press=on_key_press) as listener:
    listener.join()