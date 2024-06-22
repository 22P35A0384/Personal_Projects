n = int(input())
if (n<199):
    r = 1.20
    c = n*r
elif (200<=n<400):
    r = 1.40
    c = n*r
elif (400<=n<600):
    r = 1.60
    c = n*r
elif (600<=n<800):
    r = 1.80
    c = n*r
elif (n>=800):
    r = 2.00
    c = n*r
if (c>=400):
    a = c+c*0.15
    s = c*0.15
else:
    a = c
    s = 0.00
print('''Units Consumed: {}
Cost per Unit: {:.2f}
Bill: {:.2f}
Surcharge: {:.2f}
Total Amount: {:.2f}'''.format(n,r,c,s,a))
