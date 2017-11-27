import numpy as np
import cv2


def main():
    cap = cv2.VideoCapture(0)
    while cap.isOpened():
        _, img = cap.read()
        bw = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        _, bin =cv2.threshold(bw, 0, 255,
                              cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
        cv2.hsv
        kern = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,
                                         (3,3))
        bin = cv2.morphologyEx(bin, cv2.MORPH_OPEN, kern,
                               iterations= 3)
        dist = cv2.distanceTransform(bin, cv2.cv.CV_DIST_L2,5)
        _, sure_fg = cv2.threshold(dist, 0.5*dist.max(),255,0)
        sure_fg = np.uint8(np.around(sure_fg))

        cnt, _ = cv2.findContours(bin, cv2.RETR_EXTERNAL,
                                  cv2.CHAIN_APPROX_SIMPLE)
        i = 0
        for c in cnt:
            if c is None:
                break
            area = cv2.contourArea(c)
            if area<300:
                continue
            if len(c) < 5:
                continue
            ell = cv2.fitEllipse(c)
            cv2.ellipse(img, ell, (0,255,0), 2)
        cv2.imshow("1", img)

        if cv2.waitKey(20) & 0xff == 27:
            break
    cap.release()
cv2.destroyAllWindows()
if __name__ == '__main__':
    main()