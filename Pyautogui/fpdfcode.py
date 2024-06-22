import fpdf
pdf = fpdf.FPDF()
import csv
with open("data1.csv")as f1:
    data = list(csv.reader(f1))
    data = data[1:]
l = []
k = []
for d in data:
    x = d[2]
    y = d[3]
    l.append(x)
    k.append(y)
for i in range(len(l)):
    pdf.add_page("L")
    pdf.image("sample2.jpg",0,0,297,210)
    pdf.set_font("Times","B",20)
    pdf.set_xy(15,134)
    x = l[i],k[i]
    pdf.cell(0,0,str(x))
    pdf.output("certificates/"+"cer"+".pdf")
