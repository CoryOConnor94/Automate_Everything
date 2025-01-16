from fpdf import FPDF

pdf = FPDF(orientation='P', unit='pt', format='A4')
pdf.add_page()

pdf.image('images.jpg', w=80, h=50)

pdf.set_font(family='Times', style='B', size=24)
pdf.cell(w=0, h=50, txt='Smily Face', align='C', ln=1)

pdf.set_font(family='Times', style='B', size=14)
pdf.cell(w=0, h=15, txt='Description', ln=1)

pdf.set_font(family='Times', style='B', size=12)
text_one = """
This is a sample description for the test PDF
This will be displayed on multiple lines
Easy so far!
"""
pdf.multi_cell(w=0, h=15, txt=text_one)

pdf.set_font(family='Times', style='B', size=14)
pdf.cell(w=100, h=25, txt='Type:')

pdf.set_font(family='Times', style='B', size=14)
pdf.cell(w=100, h=25, txt='OG', ln=1)

pdf.set_font(family='Times', style='B', size=14)
pdf.cell(w=100, h=25, txt='Type:')

pdf.set_font(family='Times', style='B', size=14)
pdf.cell(w=100, h=25, txt='OG', ln=1)

pdf.output('output.pdf')