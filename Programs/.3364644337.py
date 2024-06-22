n = int(input())
l = []
for i in range(n):
    o = input().split()
    if o(0) == 'insert':
        l.insert(int(o[1]),int(0[2]))
    print(l)
    l.remove(int(o[1]))
    l.append(int(0[1]))
    elif o[0]='sort':
        l.sort()
    elif o[0]='pop':
        l.pop()
    elif o[0]='reverse':
        l.reverse()
    print(l)
    
