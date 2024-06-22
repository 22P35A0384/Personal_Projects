d,c = map(int,input().split())
a1,a2,a3 = map(int,input().split())
b1,b2,b3 = map(int,input().split())
x = a1+a2+a3
y = b1+b2+b3
if (x>=150 and y>=150):
    j = x+y+c
    i = x+y+d+d
elif (x>=150 and y<150):
    j = x+y+c+d
    i = x+y+d+d
elif (x<150 and y>=150):
    j = x+y+c+d
    i = x+y+d+d
else:
    print("NO")
if (i<=j):
    print("NO")
elif (c==d):
    print("NO")
elif (i>j):
    print("YES")
else:
    print("NO")
