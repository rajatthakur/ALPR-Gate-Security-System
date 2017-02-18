from extractMod import extractimg
from MakeRequest import *
from FileDB import *
import cv2

def strip_non_ascii(string):
    stripped = (c for c in string if 0 < ord(c) < 127)
    return ''.join(stripped)

img = cv2.imread("c5.jpg")
text = str(extractimg(img))
text = strip_non_ascii(text)
print "Num Plate : " , text
new_Entry(text)
entry(text)

# capture = cv2.VideoCapture(0)
# best_id=0
# i = 0
# if capture:
#   while True:
#
#     ret, fgmask = capture.read()
#     if ret:
#         frame = fgmask
#         contours, hierarchy = cv2.findContours(fgmask.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
#         try: hierarchy = hierarchy[0]
#         except: hierarchy = []
#         for contour, hier in zip(contours, hierarchy):
#             (x,y,w,h) = cv2.boundingRect(contour)
#             if w > 20 and h > 20:
#                 # figure out id
#                 best_id+=1
#                 cv2.rectangle(frame, (x,y), (x+w,y+h), (255, 0, 0), 2)
#                 cv2.putText(frame, str(best_id), (x,y-5), cv2.FONT_HERSHEY_SIMPLEX,
#                         0.5, (255, 0, 0), 2)
#         print(best_id)
#         cv2.imshow("Camera Feed", fgmask)
#     key = cv2.waitKey(0)
#     if key == ord('q'):
#             break
