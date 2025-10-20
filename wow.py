import pyautogui
from win32gui import GetWindowText, GetForegroundWindow
import time
import random

def main():
    print("Loaded... watching for Fellowship window and sending key presses when game window active")
    gameTitle = "Fellowship"
    starttime=time.time()
    keys = ['left', 'right', 'up', 'down', 'space']
    while True:
        currentWindow = GetWindowText(GetForegroundWindow())
        key = random.randint(0, 4)
        if(currentWindow == gameTitle):
            print("Current window is Fellowship... pressing key: " + keys[key])
            pyautogui.press(keys[key])
        interval = random.randint(1, 60)
        time.sleep(interval - ((time.time() - starttime) % interval))

if __name__ == "__main__":
    main()

