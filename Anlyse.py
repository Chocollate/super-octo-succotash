import sys, cv2, numpy as np
from os import listdir
from os.path import isfile, join
import time
import threading
import Queue

class Worker(threading.Thread):
    def __init__(self, work_queue,num):
        super(Worker, self).__init__()
        self.work_queue = work_queue
        self.num = num


    def run(self):
        sys.stdout.write("\nПоток №"+str(self.num)+
                            " начал работу")
        while True:
            wnd = 5
            if self.work_queue.empty():
                break
            filename = self.work_queue.get()
            kern = np.ones((wnd, wnd), np.float32) * (-1)
            kern[wnd / 2, wnd / 2] = wnd * wnd
            img = cv2.imread("img/" + filename)
            dst = cv2.filter2D(img, -1, kern)
            cv2.imwrite("proc/" + filename, dst)
            sys.stdout.write("\n Поток №"+str(self.num)+": работаю над файлом "+filename)


    dir = [ f for f in listdir ("img/") if isfile(join("img/", f))]
    work_queue = Queue.Queue()
    for file in dir:
        work_queue.put(file)

    start = time.time()
    workerlist = []
    for i in range(5):
        worker = Worker(work_queue, i+1)
        workerlist.append(worker)
        worker.start()

    for x in workerlist:
        x.join()

    print "\nЗатрачено %d секунд" % (time.time() - start)

