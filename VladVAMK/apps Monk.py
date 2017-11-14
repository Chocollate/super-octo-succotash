import Tkinter as tk
import cv2
import numpy as np
import tkFileDialog


def main():
    img = np.zeros((480,640,3), np.uint8)
    flag = 1
    wnd = 3

    while True:
        if flag == 1:
            dst = cv2.blur(img, (wnd,wnd))
            text = "Mean blur"
        elif flag == 2:
            dst = cv2.GaussianBlur(img, (wnd,wnd),0)
        elif flag == 3:
            dst = cv2.medianBlur(img, wnd)
        elif flag == 4:
            dst = cv2.bilateralFilter(img, wnd, 75,75)
        elif flag == 5:
            mask = cv2.GaussianBlur(img, (wnd,wnd))
            dst = cv2.addWeighted(img, 1.5, mask, -0.5, 0)
            text = "UnSharp mask"
        font = cv2.FONT_HERSHEY_PLAIN




if __name__ == '__main__':
    main()