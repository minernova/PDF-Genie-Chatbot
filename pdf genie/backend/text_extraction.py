
import PyPDF2

def extract_text(filepath):
    with open(filepath, 'rb') as f:
        reader = PyPDF2.PdfFileReader(f)
        text = ''
        for page_num in range(reader.getNumPages()):
            text += reader.getPage(page_num).extract_text()
    return text
