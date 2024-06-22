import pyautogui
import time
import csv

with open('animal.csv') as f1:
    data = list(csv.reader(f1))

pyautogui.moveTo(779,1056)
pyautogui.click()
pyautogui.moveTo(1245,565)
pyautogui.click()
e = 0
while True:
    for d in data:
        pyautogui.write('You Are A'+d[0]+'\u1F620')
        #time.sleep(0.25)
        pyautogui.press('enter')
        e+=1
        if e==100001: 
            break
