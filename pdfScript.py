from PyPDF2 import PdfWriter, PdfReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import reportlab.rl_config

reportlab.rl_config.warnOnMissingFontGlyphs = 0
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import math

packet = io.BytesIO()
can = canvas.Canvas(packet, pagesize=letter)
pdfmetrics.registerFont(TTFont('LEMONMILK', 'LEMONMILK-Light.ttf'))

names = []
x = 107
y = 655

with open('names.txt', 'r') as fd:
    names = fd.read().split('\n')
    #reader = csv.reader(fd)
    #for row in reader:
    #    names.append(row[0])

pages = math.ceil(len(names) / 8)

for i, name in enumerate(names):
    can.setFont('LEMONMILK', 35 - len(names[i]))

    if (i % 2 == 1):
        can.drawString(x, y, names[i])
        x = 107
        y -= 155

    else:
        can.drawString(x, y, names[i])
        x += 241

can.save()
packet.seek(0)

new_pdf = PdfReader(packet)
existing_pdf = PdfReader(open("original.pdf", "rb"))

output = PdfWriter()

page = existing_pdf.pages[0]
page.merge_page(new_pdf.pages[0])
output.add_page(page)

#outputStream = open("namesToPrint" + str(pages) + ".pdf", "wb")
outputStream = open("generatedPDF" + ".pdf", "wb")
output.write(outputStream)
outputStream.close()
