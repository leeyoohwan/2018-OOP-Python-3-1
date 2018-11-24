#https://www.youtube.com/watch?v=OtqWefBqbxA 참고하여 코드 작성

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel
import check_an

class Exam1(QWidget):
    global v
    def __init__(self):
        super().__init__() #부모 클래스의 init 함수 실행
        self.initUI() #여러가지를 생성하고 설정하는 함수
    def initUI(self):
        self.btn=QPushButton('공지 확인', self) #첫 매개변수는 버튼에 들어갈 문구, 두 번째 매개변수는 나 자신에게 버튼 추가한다.
        self.btn.resize(self.btn.sizeHint()) #resize는 버튼 사이즈 조절함수 sizeHint는 버튼 문구에 적당한 크기 반환해주느 함수
        self.btn.move(20, 30) #버튼 왼쪽에서 20, 위쪽에서 30 이동
        self.setGeometry(300, 300, 400, 500) #창을 왼쪽에서 300, 위쪽에서 300에 띄우고 창크기 400X500으로 설정
        self.setWindowTitle("1") #창 제목 설정하는 함수
        self.btn.clicked.connect(v.showed)
        self.show()

class Exam2(QWidget):
    def __init__(self):
        super().__init__() #부모 클래스의 init 함수 실행
        self.initUI() #여러가지를 생성하고 설정하는 함수
    def initUI(self):
        self.setGeometry(300, 300, 400, 500) #창을 왼쪽에서 300, 위쪽에서 300에 띄우고 창크기 400X500으로 설정
        self.setWindowTitle("2") #창 제목 설정하는 함수
    def showed(self):
        show_list = check_an.gosasapar()
        for i in range(0, len(show_list)):
            lb = QLabel(show_list[i], self)
            lb.move(50, 50 + i * 20)
        self.show()




app = QApplication(sys.argv) #필수적으로 쓰는 부분 그런가보다 하고 넘어가면 될 듯?
v = Exam2() #객체 생성
w = Exam1() #객체 생성
sys.exit(app.exec_()) #app.exec_()에서 메인 loop 계속 돌다가 창을 끄거나 하면 sys.exit로 프로그램 종료

