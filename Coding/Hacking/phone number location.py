import phonenumbers
from phonenumbers import geocoder
n = input()
ph1 = phonenumbers.parse(n)
print("\nPhone Numbers Location\n")
print(geocoder.description_for_number(ph1,"en"));
