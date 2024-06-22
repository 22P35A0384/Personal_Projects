n = int(input())
k = 0 
for i in range(2,n):
    if n%i!= 0:
        k = k+1
if k == 2:
    return 1

else :
    return 0

