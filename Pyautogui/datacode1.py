import fpdf
import csv
def fun(d):
    pdf = fpdf.FPDF()
    pdf.add_page("L")
    pdf.image("sample2.jpg",0,0,297,210)
    pdf.set_font("Times","B",20)
    pdf.set_xy(16,133.5)
    pdf.cell(0,0,d[2]+" "+d[3])
    pdf.output("certificates/"+d[1]+".pdf")

with open("data1.csv")as f1:
    data = list(csv.reader(f1))
    data = data[1:]

for d in data:
    fun(d)
