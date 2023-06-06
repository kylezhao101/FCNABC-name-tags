import math
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from PyPDF2 import PdfWriter, PdfReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import reportlab.rl_config

reportlab.rl_config.warnOnMissingFontGlyphs = 0

# Define parameters
font_name = 'LEMONMILK'
font_file = 'LEMONMILK-Light.ttf'
font_size_factor = 35
x_start = 107
y_start = 655
x_increment = 241
y_increment = 155

packet = io.BytesIO()
can = canvas.Canvas(packet, pagesize=letter)

pdfmetrics.registerFont(TTFont(font_name, font_file))

names = []

with open('names.txt', 'r') as fd:
    names = fd.read().split('\n')

pages = math.ceil(len(names) / 8)

for i, name in enumerate(names):
    font_size = font_size_factor - len(name)
    can.setFont(font_name, font_size)

    if i % 2 == 1:
        can.drawString(x_start, y_start, name)
        x_start = 107
        y_start -= y_increment
    else:
        can.drawString(x_start, y_start, name)
        x_start += x_increment

can.save()
packet.seek(0)

new_pdf = PdfReader(packet)
existing_pdf = PdfReader(open("original.pdf", "rb"))

output = PdfWriter()

page = existing_pdf.pages[0]
page.merge_page(new_pdf.pages[0])
output.add_page(page)

outputStream = open("generatedPDF.pdf", "wb")
output.write(outputStream)
outputStream.close()
