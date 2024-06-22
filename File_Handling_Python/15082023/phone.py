import pyautogui
import csv
import time


pyautogui.moveTo(769,1055)
pyautogui.click()
pyautogui.moveTo(1209,500)
pyautogui.click()

with open("phone.csv") as f1:
    data = list(csv.reader(f1))

# for d in data:
#     pyautogui.write("https://wa.me/")
#     time.sleep(0.5)
#     pyautogui.write(d[0])
#     pyautogui.press("enter")
#     time.sleep(0.5)
#     pyautogui.moveTo(1732,815)
#     time.sleep(0.5)
#     pyautogui.click()
#     time.sleep(0.5)
#     pyautogui.moveTo(1578,902)
#     time.sleep(0.5)
#     pyautogui.click()
#     time.sleep(0.5)
#     pyautogui.hotkey('ctrl','v')
#     time.sleep(0.5)
#     pyautogui.press("enter")
#     time.sleep(0.5)
#     pyautogui.moveTo(1205,492)
#     time.sleep(0.5)
#     pyautogui.click()
#     time.sleep(0.5)
    
    
    

