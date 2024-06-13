from reportlab.pdfgen import canvas
from scraper import chemGHScode, Label_contents

result, title = chemGHScode("https://pubchem.ncbi.nlm.nih.gov/compound/24408")
label = Label_contents(result, title)
print(label.title, label.active_pictograms, label.signal_word, label.dict_cont)

def prod_ident():
    pass

def signal_word():
    pass

def hazard_state():
    pass

def prec_state():
    pass

def pictograms():
    pass

def supp_info():
    pass
