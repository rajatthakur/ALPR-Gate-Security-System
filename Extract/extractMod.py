from PIL import Image
from pytesseract import *
import cv2
# Importing the Opencv Library
import numpy as np
# Importing NumPy,which is the fundamental package for scientific computing with Python

def extractimg(eximg):
    # Reading Image
    img = eximg

    cv2.imwrite("Images/Original Image.jpg", img)
    # Write Image

    # RGB to Gray scale conversion
    img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    cv2.imwrite("Images/Gray Converted Image.jpg", img_gray)
    # Write Image

    # Noise removal with iterative bilateral filter(removes noise while preserving edges)
    noise_removal = cv2.bilateralFilter(img_gray, 9, 75, 75)
    cv2.imwrite("Images/Noise Removed Image.jpg", noise_removal)
    # Write Image

    # Histogram equalisation for better results
    equal_histogram = cv2.equalizeHist(noise_removal)
    cv2.imwrite("Images/After Histogram equalisation.jpg", equal_histogram)
    # Write Image
    # Morphological opening with a rectangular structure element
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
    morph_image = cv2.morphologyEx(equal_histogram, cv2.MORPH_OPEN, kernel, iterations=15)
    cv2.imwrite("Images/Morphological opening.jpg", morph_image)
    # Write Image
    # Image subtraction(Subtracting the Morphed image from the histogram equalised Image)
    sub_morp_image = cv2.subtract(equal_histogram, morph_image)
    cv2.imwrite("Images/Subtraction image.jpg", sub_morp_image)
    # Write Image

    # Thresholding the image
    ret, thresh_image = cv2.threshold(sub_morp_image, 0, 255, cv2.THRESH_OTSU)
    cv2.imwrite("Images/Image after Thresholding.jpg", thresh_image)
    # # Write Image

    # Applying Canny Edge detection
    canny_image = cv2.Canny(thresh_image, 250, 255)
    cv2.imwrite("Images/ImageCanny.jpg", canny_image)
    # # Write Image
    canny_image = cv2.convertScaleAbs(canny_image)
    # dilation to strengthen the edges
    kernel = np.ones((3, 3), np.uint8)
    # Creating the kernel for dilation
    dilated_image = cv2.dilate(canny_image, kernel, iterations=1)
    cv2.imwrite("Images/Dilation.jpg", dilated_image)
    # # Write Image
    # Finding Contours in the image based on edges
    new, contours, hierarchy = cv2.findContours(dilated_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]
    # Sort the contours based on area ,so that the number plate will be in top 10 contours
    screenCnt = None
    # loop over our contours
    for c in contours:
        # approximate the contour
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.06 * peri, True)  # Approximating with 6% error
        # if our approximated contour has four points, then
        # we can assume that we have found our screen
        if len(approx) == 4:  # Select the contour with 4 corners
            screenCnt = approx
            break
    final = cv2.drawContours(img, [screenCnt], -1, (0, 255, 0), 3)
    # Drawing the selected contour on the original image
    cv2.imwrite("Images/Image with Selected Contour.jpg", final)
    # Masking the part other than the number plate
    mask = np.zeros(img_gray.shape, np.uint8)
    new_image = cv2.drawContours(mask, [screenCnt], 0, 255, -1, )
    new_image = cv2.bitwise_and(img, img, mask=mask)
    cv2.imwrite("Images/Final_image.jpg", new_image)

    # Histogram equal for enhancing the number plate for further processing
    y, cr, cb = cv2.split(cv2.cvtColor(new_image, cv2.COLOR_RGB2YCrCb))
    # Converting the image to YCrCb model and splitting the 3 channels
    y = cv2.equalizeHist(y)
    # Applying histogram equalisation
    final_image = cv2.cvtColor(cv2.merge([y, cr, cb]), cv2.COLOR_YCrCb2RGB)
    # Merging the 3 channels
    cv2.imwrite("Images/EnhancedNumberPlate.jpg", final_image)
    # Write Image

    #cropping image
    mx = 0
    minx = 1920
    my = 0
    miny = 1920

    for i in range(4):
        a = screenCnt[i]
        mx = max(mx, a[0][1])
        minx = min(minx, a[0][1])
        my = max(my, a[0][0])
        miny = min(miny, a[0][0])

    img = eximg
    cropped = img[minx:mx, miny:my]
    cv2.imwrite("Images/cropped.jpg", cropped)
    image_file = 'Images/Final_image.jpg'
    im = Image.open(image_file)
    text = image_to_string(im)
    return text
