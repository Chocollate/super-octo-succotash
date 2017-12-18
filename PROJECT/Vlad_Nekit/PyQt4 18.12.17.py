# ~*~ coding: utf8 ~*~
import cv2
import numpy as np
import sys
from PyQt4 import QtCore, QtGui

class ShowVideo(QtCore.QObject):
    camera_port = 0
    camera = cv2.VideoCapture(camera_port)
    videoSignal = QtCore.pyqtSignal(QtGui.QImage)


    def __int__(self, parent=None):
        super(ShowVideo, self).__init__(parent)

    @QtCore.pyqtSlot()
    def startVideo(self):
        run_video = True
        while run_video:
            ret, image = self.camera.read()
            rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            height, width, chan = rgb_image.shape
            bpl = chan*width
            qt_image = QtGui.QImage(rgb_image.data,
                                    width,
                                    height,
                                    bpl,
                                    QtGui.QImage.Format_RGB888)
            self.videoSignal.emit(qt_image)

class ImageViewer(QtGui.QWidget):

    def __init__(self, parent = None):
        super(ImageViewer, self). __init__(parent)
        self.image = QtGui.QImage()
        self.setGeometry(300, 300, 1000, 700)
        self.setWindowTitle('Test')

    def paintEvent(self,_):
        painter = QtGui.QPainter(self)
        painter.drawImage(0, 0, self.image)
        self.paintImage = QtGui.QImage()

    @QtCore.pyqtSlot(QtGui.QImage)
    def setImage(self, image):
        self.image = image
        self.repaint()



class QuitButton(QtGui.QWidget):

    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self, parent)
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('QuitButton')
        quit = QtGui.QPushButton('Quit', self)
        quit.setGeometry(10, 10, 60, 35)
        self.connect(quit, QtCore.SIGNAL('clicked()'),
                     QtGui.qApp, QtCore.SLOT('quit()'))


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    image_view = ImageViewer()
    vid = ShowVideo()
    vid.videoSignal.connect(image_view.setImage)
    push = QtGui.QPushButton("Start")
    push.clicked.connect(vid.startVideo)


    qb = QtGui.QPushButton("Quit")

    vert1 = QtGui.QVBoxLayout()
    vert1.addWidget(image_view)
    vert1.addWidget(qb)
    layout = QtGui
    #qb = QtGui.QPushButton("Quit")


    vert = QtGui.QVBoxLayout()
    vert.addWidget(image_view)
    vert.addWidget(push)
    layout = QtGui.QWidget()
    layout.setLayout(vert)
    main_window = QtGui.QMainWindow()
    main_window.setCentralWidget(layout)
    main_window.show()
    sys.exit(app.exec_())