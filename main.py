from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from generate_pdf import PDFgenerator

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
