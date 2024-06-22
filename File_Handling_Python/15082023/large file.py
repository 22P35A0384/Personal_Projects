import pyautogui
import csv
import time

with open ("dr2025.csv") as f1:
    data = list(csv.reader(f1))
    data = data[1:]

##pyautogui.moveTo(697,1045)
##time.sleep(0.5)
##pyautogui.click()
##time.sleep(0.5)
##pyautogui.moveTo(281,287)
##time.sleep(0.5)
##pyautogui.click()
l = []
for d in data:
    l.append(d)
print(l)
    
##    if d[8] == 'Female':
##        if d[7] == 'ACET':
##            if d[6] == 'ECE':
##                pyautogui.write("Hello "+"Miss."+d[2]+d[3])
##                time.sleep(0.2)
##                pyautogui.write(". This Your Roll Number - "+d[1]+". Your Branch IS - "+d[6])
##                time.sleep(0.2)
##                pyautogui.write(". Your Moblie And Email Are - "+"**********"+" & "+d[5])
##                time.sleep(0.2)
##                pyautogui.write(". And You Are Studing In - "+d[7]+". You Have A Mock Interview On - "+d[9])
##                time.sleep(0.2)
##                pyautogui.write(". At - "+d[10]+". By Panel Member - "+d[11])
##                time.sleep(0.2)
##                pyautogui.press("enter")
##                time.sleep(0.2)
