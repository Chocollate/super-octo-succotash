import cv2
import numpy as np
import threading
import time
import os, os.path

lface = 0
flag = False
seconds = 0
a = 0
d = None
dir = 'D:\Programs\Programs\For Kvantorium\Programs (Code)\photo'
def Timer():
    global flag
    global seconds
    seconds = 3
    while (seconds>0):
        time.sleep(1)
        seconds = seconds-1
    flag = True
    
cap = cv2.VideoCapture(0)

cv2.namedWindow("image")

cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
print cascade

while (cap.isOpened()):
    _, img = cap.read()
    img2 = img.copy()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    face = cascade.detectMultiScale(gray, scaleFactor=1.3,
                                      minNeighbors=4,
                                      minSize=(30, 30),
                                      flags=cv2.CASCADE_SCALE_IMAGE
                                    )

    for (x, y, w, h) in face:
        cv2.rectangle(img, (x, y), (x+w,y+h), (255, 0, 0), 2)

        b = len([name for name in os.listdir(dir)])
        print b

    if len(face) != lface:
        lface = len(face)
        a = 0

        if d is None:
            d = threading.Timer(3.0, Timer)
            d.start()
        if flag:
            cv2.imwrite("photo\image-" + str(a) + str(b + 1) + ".jpg", img2)
            a = a + 1
            flag=False
            d = None
    if (a is not None) and (flag==False):
        cv2.putText(img, str(seconds), (10,300), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255),2)

    cv2.imshow("image", img)
    keypress = cv2.waitKey(20) & 0xFF
    if keypress == 27:
        break

cap.release()
cv2.destroyAllWindows()
