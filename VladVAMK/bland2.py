import cv2
import numpy as np


def main():
    cap = cv2.VideoCapture(0)
    logo = cv2.imread("logo.png")
    gray = cv2.cvtColor(logo, cv2.COLOR_BGR2GRAY)
    gray = cv2.bitwise_not(gray)
    ret, mask = cv2.threshold(
        gray,100,255,
        cv2.THRESH_BINARY
    )
    mask_inv = cv2.bitwise_not(mask)
    rows, cols, _ = logo.shape
    while (1):
        ret, img = cap.read()
        roi = img[0:rows, 0:cols]
        img_bg = cv2.bitwise_and(
            roi,
            roi,
            mask=mask_inv
        )
        img_fg = cv2.bitwise_and(
             logo,
             logo,
            mask=mask
        )
        res = cv2.add(img_bg, img_fg)
        img[0:rows, 0:cols] = res
        cv2.imshow("logo", gray)
        cv2.imshow("res", img)
        if cv2.waitKey(20) & 0xff == 27:
            break
        cap.release()
        cv2.destroyAllWindows()





if __name__ == '__main__':
    main()