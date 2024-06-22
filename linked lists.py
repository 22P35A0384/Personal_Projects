class Swathi:
    def __init__(self,nagasai):
        self.nagasai = nagasai
        self.next = None
bandaru = Swathi("")
b = bandaru
####print(bandaru)
####print(bandaru.nagasai)
##bandaru.next =Swathi("lekisha")
####print(bandaru.next.nagasai)
##bandaru.next.next =Swathi("monisha")
####print(bandaru.next.nagasai)
##bandaru.next.next.next =Swathi("swathi")
####print(bandaru.next.nagasai)

l = 'isughalirusgvnialsuhveairsukgbnvalerskghvnslidfkjn'

for i in l:
    b.next = Swathi(i)
    b = b.next
bandaru = bandaru.next
c = 0
while bandaru:
##    print(bandaru.nagasai)
    c+=1
    bandaru = bandaru.next

print(c)
