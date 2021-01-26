import json
import string
import os
from docx2pdf import convert
from docxtpl import DocxTemplate
import math

def gen_pdf(num_bills, templates):
    tmpdir = "bills//templates//"
    numdigits = math.floor(math.log10(num_bills) + 1)
    for tmp in templates:
        datadir = "bills//data//"+tmp
        for i in range(num_bills):
            filename = tmpdir+tmp+".docx"
            doc = DocxTemplate(filename)
            with open(datadir+'//Invoice'+str(i+1).zfill(numdigits)+'.json') as json_file:
                data = json.load(json_file)
            doc.render(data)
            doc.save(datadir+'//'+o+str(i+1)+'.docx')

            #exportar a PDF (libre office)
            convert(datadir+"//"+o+str(i+1)+".docx", datadir+"//Invoice"+str(i+1).zfill(numdigits)+".pdf")
            os.remove(datadir+"//"+o+str(i+1)+".docx")