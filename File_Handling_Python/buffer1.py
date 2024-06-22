import csv
with open('data.csv')as f1:
    data = list(csv.reader(f1))
    data = data[1:]
l = []
for d in data:
    if d[5] not in l:
        l.append(d[5])
for d in data:
    
