import pyautogui
from win32gui import GetWindowText, GetForegroundWindow
import time
import random
import keyboard  # make sure to install with: pip install keyboard

def main():
    print("Loaded... watching for Fellowship window and sending key presses when game window is active")
    gameTitle = "fellowship"
    keys = ['a', 'd', 'w', 's', 'space']

    while True:
        # Stop script safely if Esc is pressed
        if keyboard.is_pressed('esc'):
            print("Esc pressed, stopping script.")
            break

        currentWindow = GetWindowText(GetForegroundWindow())

        # Check if Fellowship window is active
        if gameTitle.lower() in currentWindow.lower():
            key = random.choice(keys)
            hold_time = random.uniform(0.3, 0.7)  # hold key between 0.3-0.7 seconds
            print(f"Current window: {currentWindow} — pressing '{key}' for {hold_time:.2f}s")
            pyautogui.keyDown(key)
            time.sleep(hold_time)
            pyautogui.keyUp(key)

        # Wait a short random interval before next key press
        interval = random.uniform(1.0, 3.0)  # press every 1–3 seconds
        time.sleep(interval)

if __name__ == "__main__":
    main()
