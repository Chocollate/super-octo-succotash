import numpy as np
import cv2
import os


def main():
    cap = cv2.VideoCapture(0)
    count = len(os.listdir("img"))
    a = 10000
    while True:
        img = cap.read() [1]
        b = str(a)
        cv2.imwrite("img/" + b[1:] + ".jpg", img)
        a = a + 1
        print b[1:]
        if cv2.waitKey(100) & 0xff == 27:
            break
        if a == 11000:
            break



if __name__ == '__main__':
    main()