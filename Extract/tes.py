from PIL import Image
from pytesseract import *
 
image_file = 'Final_image.jpg'
im = Image.open(image_file)
text = image_to_string(im)
print text
