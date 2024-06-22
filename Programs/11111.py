n = int(input())
if (n<199):
    c = n*1.20
    if (c<400):
        a = c+100
        print(a)
    elif (c>=400):
        a = c+(c*0.15)
        print(a)
elif (200<=n<400):
    c = n*1.50
    if (c<400):
        a = c+100
        print(a)
    elif (c>=400):
        a = c+(c*0.15)
        print(a)
elif (400<=n<600):
    c = n*1.80
    if (c<400):
        a = c+100
        print(a)
    elif (c>=400):
        a = c+(c*0.15)
        print(a)
elif (n>600):
    c = n*2.00
    if (c<400):
        a = c+100
        print(a)
    elif (c>=400):
        a = c+(c*0.15)
        print(a)
