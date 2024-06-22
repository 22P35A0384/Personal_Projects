import random
import csv
with open("data1.csv")as f1:
    data = list(csv.reader(f1))
    data = data[1:]

task = [1,2,3,4,5,6,7,8,9]
dupdata= []
while True:
    n = input()
    val = random.choice(data)
    if val[1] not in dupdata:
        t = random.choice(task)
        print(val[1],val[2],t)
        dupdata.append(val[1])
    
