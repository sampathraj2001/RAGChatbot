import pdfplumber
import fitz  # PyMuPDF

def extract_text_pdfplumber(file_path):
    with pdfplumber.open(file_path) as pdf:
        text = ''
        for page in pdf.pages:
            text += page.extract_text()
    return text

def extract_text_pymupdf(file_path):
    doc = fitz.open(file_path)
    text = ''
    for page in doc:
        text += page.get_text()
    return text

def extract_text(file_path):
    text = ""
    chunks = []
    
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            text += page_text + "\n"
            
            # Split the text into chunks based on double newlines
            paragraphs = page_text.split('\n\n')
            for paragraph in paragraphs:
                paragraph = paragraph.strip()  # Remove extra whitespace
                if len(paragraph) > 0:
                    chunks.append(paragraph)
    
    return text, chunks
