import csv
from translate import Translator

with open("text.csv")as f1:
    data = list(csv.reader(f1))
    data = data[1:]
n = input()
for d in data:
    translator= Translator(to_lang=d[0])
    translation = translator.translate(n)
    print(d[0],"-",translation)
