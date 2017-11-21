# ~*~ coding: utf8 ~*~

import cv2, numpy as np
from collections import deque
import math

if __name__ == '__main__':
    cam = cv2.VideoCapture(0)
    thresh1 = 100
    thresh2 = 200
    window = deque([])
    results = []
    for i in range(15):
        window.append(np.zeros((480,640,3), np.uint8))
    while (cam.isOpened):
        _, img = cam.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        gray = cv2.equalizeHist(gray)



        _, edges1 = cv2.threshold(gray, 40, 255,+cv2.THRESH_BINARY_INV)
        temp = np.copy(edges1)
        edges1 = temp[50:350,150:540]
        # обнаружение контуров
        edges = np.copy(edges1)
        contours, hierarchy  = cv2.findContours(edges, cv2.RETR_EXTERNAL,
                                                cv2.CHAIN_APPROX_SIMPLE)
        a = 0
        results = []
        for i in contours:
            (x,y,), r = cv2.minEnclosingCircle(i)
            sx, sy, ex, ey = cv2.boundingRect(i)
            ex = ex + sx
            ey = ey + sy
            d = math.sqrt((ex - sx)**2+(ey - sy)**2)
            sx,sy, ex, ey = map(int, [sx, sy, ex, ey])
            rect = cv2.minAreaRect(i)
            box = cv2.cv.BoxPoints(rect)
            target = np.float32(([0,0], [0,300], [300,300]))

            if d >= 15:
                results.append(np.copy(
                   edges1 [sy:ey, sx:ex]
                ))
                cv2.rectangle(img, (sx+150,sy+50),
                              (ex+150, ey+50), (255,255,0), 1)
            a = a+1

        # вывод на экран
        text = "contours = %d" \
               % len(contours)
        cv2.putText(edges1, text, (50,50), cv2.FONT_HERSHEY_PLAIN,
                    1.2, (255,255,255), 1)
        cv2.imshow("img", img)
        cv2.imshow("canny", edges1)
        key = cv2.waitKey(100) & 0xff
        if key == 27:
            break
        elif key == ord('+'):
            thresh1 = thresh1 + 10
        elif key == ord('-'):
            thresh1 = max(0, thresh1 - 10)
        elif key == ord('*'):
            thresh2 = thresh2 + 10
        elif key == ord('/'):
            thresh2 = max(0, thresh2 - 10)
        elif key == ord(' '):
            w = 0
            for res in results:
                tmp = np.copy(res)
                tmp = cv2.resize(tmp,(300,300), fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
                cv2.imshow(str(w), tmp)
                w = w+1