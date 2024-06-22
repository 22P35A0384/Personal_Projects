import pyautogui
import time

pyautogui.moveTo(697,1051)
time.sleep(0.5)
pyautogui.click()
time.sleep(0.5)
pyautogui.moveTo(1219,504)
time.sleep(0.5)
pyautogui.click()
time.sleep(0.5)

for i in range(1001):
    pyautogui.write("Sorry Peddakka")
    pyautogui.press("enter")
    time.sleep(0.2)
    
