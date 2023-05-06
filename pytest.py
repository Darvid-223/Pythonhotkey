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
        if key_event == keyboard.Key.space:

            if buffer.lower().startswith("fka "):
                controller = keyboard.Controller()

                for _ in range(len("fka ")):
                    controller.press(keyboard.Key.backspace)
                    controller.release(keyboard.Key.backspace)

                controller.type("Försäkringskassan ")
                buffer = ""

            elif buffer.lower().startswith("hla "):
                controller = keyboard.Controller()

                for _ in range(len("hla ")):
                    controller.press(keyboard.Key.backspace)
                    controller.release(keyboard.Key.backspace)

                controller.type("Handläggningsassistent ")
                buffer = ""

            elif re.match(r'\d+ /m \d+ ', buffer.lower()):
                controller = keyboard.Controller()

                for _ in range(len(buffer)):
                    controller.press(keyboard.Key.backspace)
                    controller.release(keyboard.Key.backspace)

                num1, num2 = [int(x) for x in re.findall(r'\d+', buffer)]
                product = num1 * num2
                controller.type(str(product))
                buffer = ""

            else:
                buffer = ""

        elif key_event == keyboard.Key.backspace:
            buffer = buffer[:-1]
        elif isinstance(key_event, keyboard.KeyCode) and key_event.char.isprintable():
            buffer += key_event.char.lower()
            if key_event.char == " ":
                buffer += " "
                
        print(f"Current buffer: {buffer}")  # Debugging

    except Exception as e:
        print(f"Error occurred: {e}")
        buffer = ""


# Start the listener to detect key presses and call the on_key_press function
with keyboard.Listener(on_press=on_key_press) as listener:
    listener.join()

