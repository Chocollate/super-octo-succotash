import cv2
import numpy as np
global img, flag, color
def draw_circle(event,x,y,flags,param):
    global img, flag,b,g,r
    if event == cv2.EVENT_MOUSEMOVE \
            and flag:
        color = np.array((b,g,r),np.int32)
        cv2.circle(
            img,
            (x,y),
            10,
            color,
            -1)
    elif event == cv2.EVENT_LBUTTONDOWN:
        flag = True
    elif event == cv2.EVENT_LBUTTONUP:
        flag = False


def select_color(event,x,y,flags,param):
    global img,b,g,r, pal
    if event == cv2.EVENT_LBUTTONDOWN:
        b,g,r = np.copy(pal[y, x])


def main():
    global img, flag, b,g,r, pal
    flag = False
    b,g,r = (0,0,255)
    img = np.zeros((512,512,3),
                   np.uint8)
    cv2.namedWindow("image")
    cv2.setMouseCallback("image",
                         draw_circle)
    cv2.namedWindow("palette")
    cv2.setMouseCallback("palette", select_color)
    pal = np.zeros((256,180,3), np.uint8)
    pal[:,:,2] = 255
    for i in range(256):
        for j in range(180):
            pal[i,j,0] = 180-j
            pal[i,j,1] = 256-i
    pal = cv2.resize(pal, (300,300))
    pal = cv2.cvtColor(pal, cv2.COLOR_HSV2BGR)


    while True:
        cv2.imshow("image", img)
        cv2.imshow("palette", pal)
        key = cv2.waitKey(20) & 0xff

        if key == 27:
            break
        elif key == ord(' '):
            img = np.zeros((512, 512, 3),
                           np.uint8)
    cv2.destroyAllWindows()




if __name__ == '__main__':
    main()