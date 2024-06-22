import pyautogui
import time
import csv

with open("data1.csv")as f1:
    data = list(csv.reader(f1))
    data = data[1:]

pyautogui.moveTo(
