from PyQt5.QtWidgets import QWidget, QPushButton, QLineEdit, QInputDialog, QApplication
from PyQt5.QtCore import Qt

import sys

class login(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.btn = QPushButton('Login', self)
        self.btn.move(260, 300)
        self.btn.clicked.connect(self.send)

        self.id = QLineEdit(self)
        self.id.resize(300, 32)
        self.id.move(150, 200)
        self.pw = QLineEdit(self)
        self.pw.resize(300, 32)
        self.pw.move(150, 250)

        self.setFixedSize(600, 400)
        self.setWindowTitle('Dalbits_Login')
        self.show()

    def send(self): #버튼 눌리면
        self.user_id = str(self.id.text()) #정보 전송후
        self.user_pw = str(self.pw.text())
        self.close() #창을 닫는다

    def keyPressEvent(self, e): #오버라이딩, e에는 눌린 키의 정보가 담김
        if e.key() == Qt.Key_Return: #Qt.Key_Return는 enter 키를 뜻하는 상수 그래서 enter 눌린다면
            self.user_id = str(self.id.text()) #정보 전송후
            self.user_pw = str(self.pw.text())
            self.close() #창을 닫는다


if __name__=='__main__':
    app = QApplication(sys.argv)
    ex = login()
    sys.exit(app.exec_())