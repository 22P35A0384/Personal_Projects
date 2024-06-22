import matplotlib.pyplot as plt
a = [56,1,25,103]
s = ['virat','Rohit','Jadeja','Dhoni']
c = [0.05,0.05,0.05,0.05]
plt.pie(a,labels=s,startangle=90,explode=c,autopct='%0.2f%%')
plt.show()
