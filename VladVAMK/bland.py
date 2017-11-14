import numpy as np
import cv2
import os
def main():
    a = 0

    cap = cv2.VideoCapture(0)
    _img = cv2.imread("wawa-goose.jpg")
    alpha = 1
    beta = 0
    while True:
        _img = cap.read()

        img = cv2.cvtColor(img,
                           cv2.COLOR_BGR2GRAY)
        img2 = cv2.cvtColor(_img,
                            cv2.COLOR_BGR2GRAY)

        img = cv2.resize(img, (320,240))
        img2 = cv2.resize(img2, (320, 240))

        res = cv2.addWeighted(img, alpha,
                              img2, beta,
                              1)

        cv2.imshow("img", img)
        cv2.imshow("img2", img2)
        cv2.imshow("res", res)
        key = cv2.waitKey(20) & 0xff
        if key == 27:
            break
        elif key == ord(" "):
            cv2.imwrite(
                "PhotosFirst" + str(a) + ".jpg")
            a = a + 1

        elif key == ord("+"):
            alpha = max(0, alpha - 0.1)
            beta = min(1, beta + 0.1 )
        elif key == ord("-"):
            alpha = max(1,alpha + 0.1)
            beta = max(0, beta - 0.1 )

    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()