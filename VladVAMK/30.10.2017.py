import numpy as np
import cv2



def main():
    cap = cv2.VideoCapture(0)
    a = 3
    img10 = cv2.imread("kot.jpg")
    while (cap.isOpened()):
        img10 = cap.read()
        _, img = cap.read()
        noise = np.zeros((480,640,3), np.uint8)
        cv2.randn(noise, (50,50,50), (20,20,20))
        img = img + noise


        img2 = cv2.blur(img,(a,a))
        img3 = cv2.GaussianBlur(img, (a,a),0)
        img4 = cv2.medianBlur(img, a)
        img5 = cv2.bilateralFilter(img, a, 75,75)
        shr = cv2.addWeighted(img, 1.5, img3, -0.5, 0)
        cv2.imshow("scr", img)
        cv2.imshow("mean", img2)
        cv2.imshow("gaussian", img3)
        cv2.imshow("median", img4)
        cv2.imshow("bilateral", img5)
        cv2.imshow("sharp", shr)
        key = cv2.waitKey(20) & 0xff
        if key == ord('+'):
            a = a + 2
        elif key == ord('-'):
            a = max(1, a - 2)
        elif key == 27:
            break
        elif key == ord(' '):
            cv2.imread("PhotosFirst" + str(a) + ".jpg")
            a = a + 1


if __name__ == '__main__':
    main()