import csv
with open("data1.csv")as f1:
    data = list(csv.reader(f1))
    data = data[1:]
l = []
k = []
for d in data:
    x = d[2]
    y = d[3]
    z = x,y
    k.append(z)
    print(z)
