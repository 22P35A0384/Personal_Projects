n = int(input())
if (n<199):
    c = n*1.20
    if (c<400):
        a = c
        print('''Units Consumed: {}
        Cost per Unit: {:.2f}
        Bill: {:.2f}
        Surcharge: {:.2f}
        Total Amount: {:.2f}'''.format(n,1.20,c,0.00,a))
    elif (c>=400):
        a = c+(c*0.15)
        print('''Units Consumed: {}
        Cost per Unit: {:.2f}
        Bill: {:.2f}
        Surcharge: {:.2f}
        Total Amount: {:.2f}'''.format(n,1.20,c,c*0.15,a))
elif (200<=n<400):
    c = n*1.40
    if (c<400):
        a = c
        print('''Units Consumed: {}
        Cost per Unit: {:.2f}
        Bill: {:.2f}
        Surcharge: {:.2f}
        Total Amount: {:.2f}'''.format(n,1.40,c,0.00,a)
    elif (c>=400):
        a = c+(c*0.15)
        print(a)
elif (400<=n<600):
    c = n*1.60
    if (c<400):
        a = c
        print(a)
    elif (c>=400):
        a = c+(c*0.15)
        print(a)
elif (600<=n<800):
    c = n*1.80
    if (c<400):
        a = c
        print(a)
    elif (c>=400):
        a = c+(c*0.15)
        print(a)
elif (n>800):
    c = n*2.00
    if (c<400):
        a = c
        print(a)
    elif (c>=400):
        a = c+(c*0.15)
        print(a)
