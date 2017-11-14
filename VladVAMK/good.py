import numpy as np, cv2, os

def main():
    a = 0

    cap = cv2.VideoCapture(0)




while True:
    img = cap.read()
    cv2.imshow("img", img)
    key = cv2.waitKey(20) & 0xff
    if key == 27:
        break
    elif key == ord(" "):
        cv2.imwrite("PhotosFirst" + str(a) + ".jpg")
        a = a+1
cv2.destroyAllWindows()
if __name__ == '__main__':
    main()