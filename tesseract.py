import pytesseract
from PIL import Image

img = Image.open("test_text.png")
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

text = pytesseract.image_to_string(img, lang="ukr")
print(text.strip())

with open('test_text.txt', 'a') as f:
    f.write(text.strip()+"\n")
