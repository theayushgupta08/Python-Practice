import pyautogui
import time
time.sleep(4)
count=0
while count<=1000:
    pyautogui.typewrite("Sorry babu")
    pyautogui.press("Enter")
    count=count+1

