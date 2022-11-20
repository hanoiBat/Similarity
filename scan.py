import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'C:\Users\sscha\AppData\Local\Tesseract-OCR\tesseract.exe'
def scan(path):
    return tess.image_to_string(path)