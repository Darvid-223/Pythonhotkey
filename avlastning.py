import keyboard as kb
from pynput import keyboard
import time
import re

# kommentera bort under test i vs code terminal för att inte radera texten under test
#lock_file = open(sys.argv[0], 'w')
#try:
#    fcntl.flock(lock_file, fcntl.LOCK_EX | fcntl.LOCK_NB)
#except IOError:
#    print("Another instance is already running, quitting.")
#    sys.exit(0)
# ps aux | grep python | grep -v grep
buffer = ""

def handle_hotstrings(buffer):
    if buffer.lower() == "fka":
        kb.write('\b' * (len(buffer) + 1))
        kb.write("Försäkringskassan ")
        return True

    elif buffer.lower() == "hla":
        kb.write('\b' * (len(buffer) + 1))
        kb.write("Handläggningsassistent ")
        return True

    else:
        return False

def handle_multiplication(buffer):
    if buffer.endswith("/m"):
        number_string = buffer[:-2].strip()
        
        # Check if the number_string has the correct format
        if re.match(r'^\d+\.\d+$', number_string):
            numbers = [float(n) for n in number_string.split('.')]
            result = numbers[0] * numbers[1]

            kb.write('\b' * len(buffer))
            kb.write(str(restult))
            return True

    return False


def on_key_press(key_event):
    global buffer
    time.sleep(0.05)

    try:
        if key_event == keyboard.Key.space:
            if not handle_hotstrings(buffer) and not handle_multiplication(buffer):
                buffer = ""

        elif key_event == keyboard.Key.backspace:
            buffer = buffer[:-1]

        elif isinstance(key_event, keyboard.KeyCode) and (key_event.char.isalnum() or key_event.char in [".", "/", "-"]):
            # Check if the key name is printable
            if all(c.isprintable() for c in key_event.char):
                buffer += key_event.char.lower()

    except Exception as e:
        print(f"Error occurred: {e}")
        buffer = ""



with keyboard.Listener(on_press=on_key_press) as listener:
    listener.join()
