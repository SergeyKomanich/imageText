import pytesseract
from PIL import Image

image = Image.open("text_pa.jpg")
pytesseract.pytesseract.tesseract_cmd = r"/usr/bin/tesseract"


text = pytesseract.image_to_string(image, lang="ukr")
print(text.strip())

with open('text_test.txt', 'a', encoding= 'utf-8') as file:
    file.write(text.strip() + "\n")