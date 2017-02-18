import cv2
img = cv2.imread("Final_image.jpg")
img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
ret, thresh_image = cv2.threshold(img_gray, 127, 255, cv2.THRESH_OTSU)
cv2.imwrite("Thresh.jpg", thresh_image)

