import numpy as np
import cv2
import os
from datetime import datetime

def main():
    cap = cv2.VideoCapture(0)
    count = len(os.listdir("PhotosFirst"))
    while True:
        ret, frame = cap.read()
        cv2.imshow("frame", frame)
        key = chr(cv2.waitKey(20) & 0xff)
        if key == 'q':
            break
        elif key == ' ':
            cv2.imwrite(
                "PhotosFirst/image-" + str(count) + ".jpg", frame)
            count = count + 1
    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
