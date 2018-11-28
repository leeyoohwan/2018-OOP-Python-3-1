from PyQt5.QtWidgets import QWidget, QPushButton, QLineEdit, QInputDialog, QApplication

import sys

class login(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.btn = QPushButton('Login', self)
        self.btn.move(20, 100)
        self.btn.clicked.connect(self.send)

        self.id = QLineEdit(self)
        self.id.resize(300, 32)
        self.id.move(300, 200)
        self.pw = QLineEdit(self)
        self.pw.resize(300, 32)
        self.pw.move(300, 250)

        self.setFixedSize(900, 600)
        self.setWindowTitle('Input Dialog')
        self.show()

    def send(self):
        self.user_id = str(self.id.text())
        self.user_pw = str(self.pw.text())


if __name__=='__main__':
    app = QApplication(sys.argv)
    ex = login()
    sys.exit(app.exec_())