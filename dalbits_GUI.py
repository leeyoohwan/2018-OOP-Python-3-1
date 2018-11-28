#https://stackoverflow.com/questions/41290035/pyqt-change-gui-layout-after-button-is-clicked/41290921

import sys
import parsing

from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel

class UIWindow(object):
    def setupUI(self, MainWindow):
        MainWindow.setFixedSize(640, 480)
        MainWindow.setWindowTitle("Dalbits")
        self.centralwidget = QWidget(MainWindow)
        self.ToolsBTN = QPushButton('text', self.centralwidget)
        self.ToolsBTN.move(50, 350)
        MainWindow.setCentralWidget(self.centralwidget)
        self.lb = QLabel(self.centralwidget)
        text=parsing.sub_get_insert_time_and_press('https://store.musinsa.com/app/contents/bestranking')
        self.lb.setText(text)
        self.lb.move(50, 350)


class UIToolTab(object):
    def setupUI(self, MainWindow):
        MainWindow.setFixedSize(640, 480)
        self.centralwidget = QWidget(MainWindow)
        self.CPSBTN = QPushButton("text2", self.centralwidget)
        self.CPSBTN.move(100, 350)
        MainWindow.setCentralWidget(self.centralwidget)

"""
class StartDalbits(object):
    def setupUI(self, MainWindow):
        MainWindow.setFixedSize(640, 480)
        self.centralwidget = QWidget(MainWindow)
        MainWindow.setCentralWidget(self.centralwidget)

        videoWidget = QVideoWidget()
        self.playButton = QPushButton()
        self.playButton.setEnabled(False)
        self.playButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        self.playButton.clicked.connect(self.play)
"""


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.uiWindow = UIWindow()
        self.uiToolTab = UIToolTab()
        self.startUIWindow()

    def startUIToolTab(self):
        self.uiToolTab.setupUI(self)
        self.uiToolTab.CPSBTN.clicked.connect(self.startUIWindow)
        self.show()

    def startUIWindow(self):
        self.uiWindow.setupUI(self)
        self.uiWindow.ToolsBTN.clicked.connect(self.startUIToolTab)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    sys.exit(app.exec_())