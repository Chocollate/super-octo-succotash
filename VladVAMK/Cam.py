import cv2, numpy as np
from datetime import datetime
NUM_CAMERAS = 4
SCREEN_X = 1920
SCREEN_Y = 1080

def main():
    cap = []
    for i in range(NUM_CAMERAS):
        cap.append(cv2.VideoCapture(0))
    cv2.namedWindow("img", cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty("img", cv2.WND_PROP_FULLSCREEN, cv2.cv.CV_WINDOW_FULLSCREEN)

    while True:
        img = []
        cam_x = SCREEN_X / (NUM_CAMERAS / 2)
        cam_y = SCREEN_Y / (NUM_CAMERAS / 2)
        for i in range(NUM_CAMERAS):
            ret, tmp = cap[i].read()
            tmp = cv2.resize(tmp,(cam_x, cam_y))
            font = cv2.FONT_HERSHEY_PLAIN
            cv2.putText(tmp, "Camera" + str(i),
                        (10, cam_y-20), font, 1,
                        (255,255,255))
            cv2.rectangle(tmp, (0,0), (cam_x,cam_y),
                          (255,0,0),4)
            img.append(tmp)
        screen = np.zeros((SCREEN_Y,
                           SCREEN_X,
                           3),np.uint8)
        i = 0
        for x in range(NUM_CAMERAS/2):
            for y in range(NUM_CAMERAS/2):
                screen[y*cam_y:(y+1)*cam_y,
                x*cam_x:(x+1)*cam_x] = img[i]
                i = i+1
        a = datetime.now().strftime("%d. %m. %Y %H:%M:%S")
        cv2.putText(tmp, "Camera" + str(i),
                        (10, cam_y - 20), font, 1,
                        (255, 255, 255))


        cv2.imshow("img", screen)
        key = cv2.waitKey(20) & 0xff
        if key == 27:
            break
#    for i in range (NUM_CAMERAS):




if __name__ == '__main__':
    main()







