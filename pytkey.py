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
    

buffer = ""  
# Calls function när tangent trycks
def on_key_press(key_event):
    global buffer
    try:
        # If the space key is pressed
        if key_event == keyboard.Key.space:
            # Check if the buffer contains "fka"
            if buffer.lower() == "fka":
                controller = keyboard.Controller()

                # Remove the typed abbreviation and the space
                for _ in range(len(buffer) + 1):
                    controller.press(keyboard.Key.backspace)
                    controller.release(keyboard.Key.backspace)

                controller.type("Försäkringskassan ")
                buffer = ""

            # Check if the buffer contains "hla"
            elif buffer.lower() == "hla":
                controller = keyboard.Controller()

                for _ in range(len(buffer) + 1):
                    controller.press(keyboard.Key.backspace)
                    controller.release(keyboard.Key.backspace)

                controller.type("Handläggningsassistent ")
                buffer = ""

            # If the buffer doesn't contain "hla" or "fka", clear the buffer
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