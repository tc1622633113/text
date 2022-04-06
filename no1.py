from matplotlib.pyplot import box
import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
img = cv2.imread(r"C:\Users\16226\Documents\study\1.jpg")
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
#print(pytesseract.image_to_string(img))

#Detecting Characters
hImg,wImg,_ = img.shape
boxes = pytesseract.image_to_boxes(img)
for b in boxes.splitines():
    print(b)
    

cv2.imshow("result",img)
cv2.waitKey(0)
