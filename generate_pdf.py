# from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
# from reportlab.platypus import Paragraph

from PyPDF2 import PdfFileWriter, PdfFileReader

from datetime import datetime

import io

pdfmetrics.registerFont(TTFont('THSaraban', './fonts/THSarabunNew.ttf'))
pdfmetrics.registerFont(TTFont('Prompt', './fonts/Prompt-Regular.ttf'))


def PDFgenerator(FormCleanData: dict):

    buffer = io.BytesIO()

    page_break = 115

    c = canvas.Canvas(buffer, pagesize=letter)
    textObj = c.beginText()
    textObj.setTextOrigin(52, 719)
    textObj.setFont("Prompt", 14)

    textObj.textLine(f"Information and Digital Technology Center (IDT)")
    textObj.setFont("THSaraban", 18)
    textObj.textLine('-'*page_break)

    for k, v in FormCleanData.items():
        # by pass render desc
        if k == "desc":
            continue

        textFormat = f"{k}: {v}"
        textObj.textLine(textFormat)

    timenow = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    textObj.textLine(f"timestamp: {timenow}")

    textObj.textLine('-'*page_break)
    textObj.textLines(
        f"""note:\n{v}""")

    c.drawText(textObj)
    c.showPage()

    c.save()

    buffer.seek(0)
    # write to buffer

    out = PdfFileWriter()

    file = PdfFileReader(buffer)
    num = file.numPages

    for idx in range(num):
        page = file.getPage(idx)
        out.addPage(page)

    password = "123456"
    out.encrypt(password)
    out.write(buffer)

    buffer.seek(0)
    # write to buffer #encrypt file

    # return bytes
    return buffer
