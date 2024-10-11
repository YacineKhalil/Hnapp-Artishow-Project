import cv2  #premiere utilisation sur un pc : pip install cv2
import pytesseract  #premiere utilisation sur un pc : installer tesseract (voir internet) puis pip install pytesseract 
#C:\Program Files\Tesseract-OCR
from pytesseract import Output

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  #ici on précise l'endroit où se trouve le logiciel tesseract pour pouvoir l'appeler

img = cv2.imread('sample3.jpg')

d = pytesseract.image_to_data(img, output_type=Output.DICT)
print(d.keys())

n_boxes = len(d['text'])
for i in range(n_boxes):
    if int(d['conf'][i]) > 60:
        (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
        img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

cv2.imshow('img', img)
cv2.waitKey(0)