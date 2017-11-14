import cv2, numpy as np

if __name__ == '__main__':
    cap = cv2.VideoCapture(1)
    cap2 = cv2.VideoCapture(0)
    while cap.isOpened():
        _, img = cap.read()
        _, img2 = cap2.read()
        G = img.copy()
        gp1 = [G]
        for i in xrange(6):
            G = cv2.pyrDown(G)
            gp1.append(G)
        G = img2.copy()
        gp2 = [G]
        for i in xrange(6):
            G = cv2.pyrDown(G)
            gp2.append(G)
        lp1 = [gp1[5]]
        for i in xrange(5, 0, -1):
            GE = cv2.pyrUp(gp1[i])
            L = cv2.subtract(gp1[i - 1], GE)
            lp1.append(L)
        lp2 = [gp2[5]]
        for i in xrange(5, 0, -1):
            GE = cv2.pyrUp(gp2[i])
            L = cv2.subtract(gp2[i - 1], GE)
            lp2.append(L)
        LS = []
        for la, lb in zip(lp1, lp2):
            r, c, _ = la.shape
            ls = np.vstack((la[0:r/2, :], lb[r/2:, :]))
            LS.append(ls)
        ls_ = LS[0]
        for i in xrange(1,6):
            ls_ = cv2.pyrUp(ls_)
            ls_ = cv2.add(ls_, LS[i])

        cv2.imshow("z", ls_)
        if cv2.waitKey(20) & 0xff == 27:
            break
    cap.release()
    cv2.destroyAllWindows()


