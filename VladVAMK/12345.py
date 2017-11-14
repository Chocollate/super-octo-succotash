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
        cv2.imshow("frame", img)
        key = chr(cv2.waitKey(20) & 0xff)
        if key == 'q':
            break
        elif key == ' ':
            cv2.imwrite(
                "img/" + str(count) + ".jpg", img)
            count = count + 1
        print b[1:]


if __name__ == '__main__':
    main()