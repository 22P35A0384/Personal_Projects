import csv
with open('data1.csv')as f1:
          data = list(csv.reader(f1))
          data = data[1:]
aecmech = 0
aeceee = 0
acetmech = 0
aceteee = 0
acoeeee = 0
acoemech = 0
for d in data:
    if d[6]=='AEC':
        if d[5]=='MECH':
            aecmech+=1
        if d[5]=='EEE':
            aeceee+=1
    if d[6]=='ACET':
        if d[5]=='MECH':
            acetmech+=1
        if d[5]=='EEE':
            aceteee+=1
    if d[6]=='ACOE':
        if d[5]=='MECH':
            acoemech+=1
        if d[5]=='EEE':
            acoeeee+=1
import matplotlib.pyplot as plt
a = [aecmech,aeceee,acetmech,aceteee,acoemech,acoeeee]
b = ['AEC-MECH','AEC-EEE','ACET-MECH','ACET-EEE','ACOE-MECH','ACOE-EEE']
c = [0.05,0.05,0.05,0.05,0.05,0.05]
plt.pie(a,labels=b,explode=c,autopct='%0.2f%%',startangle=90)
plt.title('Mech & Eee Students Statistics')
plt.show()


