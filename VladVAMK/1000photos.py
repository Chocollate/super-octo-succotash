import numpy as np, cv2


def main():
    cap = cv2.VideoCapture(0)
    a = 10000
while True:
    _, img = cap.read() [1]
    b = str(a)
    cv2.imwrite("img/"+b[1:]+".jpg",img)
    a = a+1
    print b[1:]
    if cv2.waitKey(100) & 0xff == 27:
        break
    if a == 11000:
        break
cap.release()



if __name__ == '__main__':
    main()