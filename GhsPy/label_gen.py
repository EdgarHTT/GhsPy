from reportlab.platypus import Paragraph, Frame, SimpleDocTemplate, KeepInFrame
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm
from reportlab.lib.styles import getSampleStyleSheet



def prod_ident(pdf):
    #Text in paragraph obj
    p_text = Paragraph(label.title, style = Styles["Normal"])

    #Added to the flow_obj, #TODO: learn more
    flow_obj.append(p_text)

    #Frame
    frame_t = Frame(pos_x , pos_y + height-((height/6) * 1), 200, height/6, showBoundary = 1)

    #To the frame obj it is appended the flow_obj with the paragraph obj within
    frame_t.addFromList(flow_obj, pdf)
    
def signal_word(pdf):
    p_text = Paragraph(label.signal_word, style = Styles["Normal"])
    flow_obj.append(p_text)
    frame_sig = Frame(pos_x , pos_y + height-((height/6) * 2), 200, height/6, showBoundary = 1)
    frame_sig.addFromList(flow_obj, pdf)
    
def hazard_state(pdf):
    p_text = ""
    for code in list(label.hazard_cont.keys()):
        p_text = p_text + code + ": " + label.hazard_cont[code][0] + " "
    p_text = Paragraph(p_text, style = Styles["Normal"])
    #TODO learn more about the KeepInFrame method, add it to the other funcs
    p_text_inframe = KeepInFrame(flow_obj.append(p_text)
    frame_haz = Frame(pos_x , pos_y + height-((height/6) * 3), 200, height/6, showBoundary = 1)
    frame_haz.addFromList(flow_obj, pdf)
    
def prec_state(pdf):
    frame_prec = Frame(pos_x , pos_y, 200, height/2, showBoundary = 1)
    frame_prec.addFromList(flow_obj, pdf)

def pictograms(pdf):
    frame_picto = Frame(pos_x + base/2 , pos_y, 200, 200, showBoundary = 1)
    frame_picto.addFromList(flow_obj, pdf)

def supp_info(pdf):
    pass

pdf = canvas.Canvas("Frame.pdf")

#Global label dimensions and original position
height = 200
base = 400
pos_x = 20
pos_y = 20

#
flow_obj = []
Styles = getSampleStyleSheet()

#Frame and paragraph generation
prod_ident(pdf)
signal_word(pdf)
hazard_state(pdf)
prec_state(pdf)
pictograms(pdf)

#pdf saving
pdf.save()

#https://www.youtube.com/watch?v=hhJm86YllP8&list=PLI8raxzYtfGzwEqGLm4fCnnbTAGbSHa6-&index=23
#https://stackoverflow.com/questions/12014573/reportlab-how-to-auto-resize-text-to-fit-block