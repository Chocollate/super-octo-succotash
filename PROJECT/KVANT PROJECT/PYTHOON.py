import cv2
import numpy


cap = cv2.VideoCapture(0)
while cap.isOpened():
    _, img = cap.read()
    cv2.imshow("img", img)
    key = cv2.waitKey(20) & 0xff
    if key == (27):
        break
cap.release()
cv2.destroyAllWindows()