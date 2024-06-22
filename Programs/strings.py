##s = "string slicing"
##print(s[8])
##print(s[10:13])
##print(s[1::2])
##print(s[-12])
##print(s[-7:-4])
##print(s[::-1])


##s1 = input()
##s2 = input()
##if s2 in s1:
##    print("Found")
##else:
##    print("Not Found")


##s = "jami venkata sai gangadhar"
##s1 = input()
##x = (s.replace('jami venkata sai ',s1))
##print(x)


##s = input()
##x = s.upper()
##print(x)
##s1 = input()
##y = s1.lower()
##print(y)


##n = input()
##v = input()
##x = n.isalpha()
##y = n.isalnum()
##if x == True:
##    print("ok")
##else:
##    print("not ok")
##if y == True:
##    print("ok")
##else:
##    print("Not ok")


##n = input()
##print(n.strip())


##v = input()
##print(v.lstrip())


##x = input()
##print(x.rstrip())
##s = "Jami Venkata Sai Gangadhar"
##print(s.split())


##n = input()
##x = n[::-1]
##y = len(n)
##a = y//2
##if (y%2==0):
##    b = n[:a]
##    c = n[a:]
##else:
##    b = n[:a]
##    c = n[a+1:]
##if (n == x):
##    print("palindrome")
##if(b==c):
##    print("Symmetrical")
##else:
##    print("Not Palindrome and Not Symmetrical")



##n = input()
##l = list(n)
##x = len(n)
##for i in range(x//2):
##    l[i],l[x-i-1]= l[x-i-1],l[i]
##print("".join(l))

m = input()
l = list(m)
x = len(m)
for i in range(x):
    a = l.isalpha()
    if (a == True):
        break
for i in range(x):
    b = l.isalnum()
    if (b == True):
        break
if (a == True, b == True):
    print("OK")
else:
    print("Not OK")
