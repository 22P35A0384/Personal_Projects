import pyautogui
import csv

pyautogui.moveTo(814,1049)
pyautogui.click()
pyautogui.moveTo(1214,477)
pyautogui.click()
with open("text.csv") as f1:
    data = list(csv.reader(f1))
    data = data[1:]
for d in data:
    print(d)
##    pyautogui.write(d[0]+" - "+d[1])
##    pyautogui.press("enter")
