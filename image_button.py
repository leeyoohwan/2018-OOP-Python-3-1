#https://stackoverflow.com/questions/23634241/put-an-image-on-a-qpushbutton 참고해서 작성

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import QSize

class Exam(QWidget):
    def __init__(self):
        super().__init__() #부모 클래스의 init 함수 실행
        self.initUI() #여러가지를 생성하고 설정하는 함수
    def initUI(self):
        self.btn=QPushButton('', self) #첫 매개변수는 버튼에 들어갈 문구, 두 번째 매개변수는 나 자신에게 버튼 추가한다.
        #icon=QPixmap("image.jpg")
        self.btn.setIcon(QIcon("image.png")) #버튼에 들어갈 이미지 지정
        self.btn.move(20, 30) #버튼 왼쪽에서 20, 위쪽에서 30 이동
        self.btn.setIconSize(QSize(100, 100)) #버튼에 들어가는 이미지의 크기 지정
        self.setGeometry(300, 300, 400, 500) #창을 왼쪽에서 300, 위쪽에서 300에 띄우고 창크기 400X500으로 설정
        self.setWindowTitle("첫 번째 학습시간") #창 제목 설정하는 함수
        self.show()  # 창 띄우기

app = QApplication(sys.argv) #필수적으로 쓰는 부분 그런가보다 하고 넘어가면 될 듯?
w = Exam() #객체 생성
sys.exit(app.exec_()) #app.exec_()에서 메인 loop 계속 돌다가 창을 끄거나 하면 sys.exit로 프로그램 종료