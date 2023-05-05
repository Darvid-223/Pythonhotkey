from pynput import keyboard

buffer = ''  # Initialize an empty string buffer to store keystrokes

# This function will be called every time a key is pressed
def on_key_press(key_event):
    global buffer  # We use the global buffer variable

    # If the space key is pressed, check if the buffer contains "fk"
    if key_event == keyboard.Key.space:
        if buffer.lower() == 'fk':
            controller = keyboard.Controller()
            # Press the backspace key twice to remove "fk"
            for _ in range(3):
                controller.press(keyboard.Key.backspace)
                controller.release(keyboard.Key.backspace)
            # Then, type "Försäkringskassan" instead
            controller.type('Försäkringskassan')
        buffer = ''  # Clear the buffer after the space key is pressed
    # If the backspace key is pressed, remove the last character from the buffer
    elif key_event == keyboard.Key.backspace:
        buffer = buffer[:-1]
    # If a printable character key is pressed, add it to the buffer
    elif isinstance(key_event, keyboard.KeyCode) and key_event.char.isprintable():
        buffer += key_event.char.lower()

# Start the listener to detect key presses and call the on_key_press function
with keyboard.Listener(on_press=on_key_press) as listener:
    listener.join()
