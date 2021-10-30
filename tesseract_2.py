import pytesseract
from PIL import Image

img = Image.open("image_with_phone.png.png")
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

custom_config = r'--oem 3 --psm 13'
text = pytesseract.image_to_string(img, config=custom_config)
print(text.strip())

with open('phone_numbers.txt', 'a') as f:
    f.write(text.strip()+"\n")