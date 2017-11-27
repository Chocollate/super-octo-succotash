import numpy as np
import cv2
from matplotlib import pyplot as plt

cap = cv2.VideoCapture(0)
while cap.isOpened():
    _, img = cap.read()
    if img.shape [-1] == 3: # Цветное изображ
        b, g, r, = cv2.split (img) # get b, g, r
        rgb_img = cv2.merge([r, g, b]) # Переключ на rgb
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    else:
        gray_img = img

    Img =  cv2.medianBlur(gray_img, 5)
    cimg = cv2.cvtColor(Img, cv2.COLOR_GRAY2BGR)

    circles = cv2.HoughCircles(Img, cv2.HOUGH_GRADIENT, 1,20,
                               param1 = 50, param2 = 30, minRadius = 0, maxRadius = 0)

    circles = np.uint16 (np.around(circles))

    for i in circles [0,:] :
        # нарисовать внешний круг
        cv2.circle(cimg, (i [0], i [1]), i [2], (0,255,0), 2)
        # Нарисовать центр круга
        cv2.circle(cimg, (i [0], i [1]), 2, (0,0,255), 3)


    cv2.imshow('img', img)

    key = cv2.waitKey(20) & 0xff
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()