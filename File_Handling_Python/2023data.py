import csv
with open('2023acet.csv') as f1:
    data = list(csv.reader(f1))
    data = data[1:]
for d in data:
    print(d[0])