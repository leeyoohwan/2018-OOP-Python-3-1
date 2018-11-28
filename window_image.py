#https://pythonspot.com/pyqt5-image/ 참고하여 작성
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QIcon, QPixmap


class App(QWidget):

    def __init__(self):
        super().__init__()
        self.left = 500
        self.top = 500
        self.width = 640
        self.height = 480
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Exam")
        label = QLabel(self)
        pixmap = QPixmap('image.png')
        label.setPixmap(pixmap)
        self.setFixedSize(pixmap.width(), pixmap.height())
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())