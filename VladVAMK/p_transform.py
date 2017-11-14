import numpy as np, cv2


def click(event, x,y, flags, param):
    global points
    if event == cv2.EVENT_LBUTTONDOWN:
        if len(points) < 4:
            points.append((x,y))
    elif event == cv2.EVENT_RBUTTONDOWN:
        points = []

def main():
    global points
    points = []
    trans = np.zeros((500, 500, 3), np.uint8)
    test = np.zeros((500,500,3), np.uint8)
    cap = cv2.VideoCapture(0)

    cv2.namedWindow("camera")
    cv2.namedWindow("result")
    cv2.setMouseCallback("camera", click)

    while (cap.isOpened()):
        _, img = cap.read()
        if len(points) == 1:
            cv2.circle(img, points[0], 4,
                       (0, 255, 0), -1)
        elif 1 < len(points) < 4:
            cv2.circle(img, points[0], 4,
                       (0, 255, 0), -1)
            for i in range(1, len(points)):
                cv2.line(
                    img,
                    points[i - 1],
                    points[i],
                    (0, 255, 0),
                    2
                )
                cv2.circle(img, points[0], 4,
                           (0, 255, 0), -1)
        elif len(points) == 4:
            pts1 = np.float32(points)
            pts2 = np.float32([0, 500], [0, 0],
                              [500, 0], [500, 500])
            M = cv2.getPerspectiveTransform(pts1, pts2)
            trans = cv2.warpPerspective(img, M, (500, 500))
            trans = cv2.cvtColor(trans, cv2.COLOR_BGR2GRAY)
            clahe = cv2.createCLAHE(clipLimit= 2.0,
                                    tileGridSize=(8,8) )
            cv2.circle(img, points[0], 4,
                       (0, 255, 0), -1)
            for i in range(1, len(points)):
                cv2.line(
                    img,
                    points[i-1],
                    points[1],
                    (0,255,0),
                    2
                )
                cv2.circle(img, points[0], 4,
                           (0, 255, 0), -1)
                cv2.line(
                    img,
                    points[i - 1],
                    points[1],
                    (0, 255, 0),
                    2
                )

            else:
                points = []

                cv2.imshow("camera", img)
                cv2.imshow("equ", test)
                _, thresh1 = cv2.threshold(test, 127, 255, cv2.THRESH_BINARY)

                thresh2 = cv2.adaptiveThreshold(test,
                                                255,
                                                cv2.ADAPTIVE_THRESH_MEAN_C,
                                                cv2.THRESH_BINARY,
                                                11,
                                                2
                                            )
                thresh3 = cv2.adaptiveThreshold(test,
                                                255,
                                                cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                                cv2.THRESH_BINARY,
                                                11,
                                                2
                                                )

                cv2.imshow("binary", thresh1)
                cv2.imshow("mean", thresh2)
                cv2.imshow("gaussian", thresh3)




        key = cv2.waitKey(20) & 0xff
        if key == 27:
            break



if __name__ == '__main__':
    main()
