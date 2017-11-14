#~*~ coding: utf8 ~*~
import time, sys, cv2, numpy as np
from os import listdir
from os.path import isfile, join
from multiprocessing import Pool



def work(filename):
    wnd = 11
    kern = np.ones((wnd, wnd), np.float32) * (-1)
    kern[wnd / 2, wnd / 2] = wnd * wnd
    img = cv2.imread("img/" + filename)
    img = cv2.GaussianBlur(img, (21,21), 0)
    dst = cv2.filter2D(img, -1, kern)
    cv2.imwrite("proc2/" +filename, dst)

if __name__ == '__main__':
    files = [f for f in listdir("img/") if isfile(join("img/", f))]


    p = Pool(12)
    start = time.time()
    p.map(work, files)
    print "Заняло: %d секунд" % (time.time()-start)

















