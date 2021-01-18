import replace_field
import word_generator

num_bills = 1
templates = ["Endesa2019bis", "Repsol2020", "Naturgy2015", "Naturgy2019", "Iberdrola2013", "Endesa2019", "Endesa2012bis", "Endesa2012"]
replace_field.gen_json(num_bills, templates)
word_generator.gen_pdf(num_bills, templates)