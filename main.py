from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from generate_pdf import PDFgenerator

from generate_fpdf import test_fpdf

import io

app = FastAPI()

@app.get("/generate")
def main():

    input = {
        "key": "values"
    }

    buffer = PDFgenerator(input)

    response = StreamingResponse(buffer, media_type="application/pdf")
    response.headers["Content-Disposition"] = "attachment; filename=files_pdf.pdf"

    return response

@app.get("/fpdf")
def main_fpdf():

    buffer = test_fpdf()

    bio = io.BytesIO(buffer) 

    response = StreamingResponse(bio, media_type="application/pdf")
    response.headers["Content-Disposition"] = "attachment; filename=files_pdf.pdf"

    return response

