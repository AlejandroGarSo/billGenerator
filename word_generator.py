import json
import string
import os
from docx2pdf import convert
from docxtpl import DocxTemplate

def gen_pdf(num_bills, templates):
    tmpdir = "bills//templates//"
    for tmp in templates:
        datadir = "bills//data//"+tmp
        for i in range(num_bills):
            filename = tmpdir+tmp+".docx"
            doc = DocxTemplate(filename)
            with open(datadir+'//'+str(i+1)+'.json') as json_file:
                data = json.load(json_file)
            doc.render(data)
            doc.save(datadir+'//'+str(i+1)+'.docx')

            #exportar a PDF (libre office)
            convert(datadir+"//"+str(i+1)+".docx", datadir+"//"+str(i+1)+".pdf")
            os.remove(datadir+"//"+str(i+1)+".docx")