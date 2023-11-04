import pyautogui
import time

time.sleep(4)

f= open("messages.txt","r", encoding="utf-8")

for word in f:
    pyautogui.typewrite(word)
    pyautogui.press("enter")



