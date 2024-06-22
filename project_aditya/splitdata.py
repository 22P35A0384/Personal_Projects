import csv

with open('maindata.csv', newline='', encoding='utf-8') as f1 :
    data = list(csv.reader(f1))
    data = data[1:]

# x = {}
# for d in data:
#     if d[1] not in x:
#         x[d[1]] = 1
#     else:
#         x[d[1]]+=1
# print(x)


# y = []
# for d in data:
#     if len(d[3])==10:
#         y.append(d[3])

# print(y)
# print(len(y))

x = []
for d in data:
    x.append(d[3])
y={}

for i in x:
    if x.count(i)>1:
        if i not in y:
            y[i]=1
        else:
            y[i]+=1

with open('log2.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    for a,b in y.items():
        writer.writerow([a,b])

print(y)
print(len(y))

# x = {'a':1,'b':2}
# for i,j in x.items():
#     print(i,j)