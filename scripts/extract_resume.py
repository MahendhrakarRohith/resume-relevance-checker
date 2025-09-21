from PyPDF2 import PdfReader
from docx import Document

def extract_pdf(file):
    pdf = PdfReader(file)
    text = ""
    for page in pdf.pages:
        text += page.extract_text()
    return text

def extract_docx(file):
    doc = Document(file)
    text = "\n".join([p.text for p in doc.paragraphs])
    return text
