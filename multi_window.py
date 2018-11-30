#https://www.youtube.com/channel/UCFinQvpLueFGR431gRsltOQ 참고하여 코드 작성

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QVBoxLayout, QMessageBox
from PyQt5.QtGui import QIcon, QPixmap, QFont
import check_an
from PyQt5.QtCore import Qt

class Exam1(QWidget):
    global v
    def __init__(self):
        super().__init__() #부모 클래스의 init 함수 실행
        self.initUI() #여러가지를 생성하고 설정하는 함수
    def initUI(self):
        label = QLabel(self)
        pixmap = QPixmap('background.png')
        label.setPixmap(pixmap)
        self.setFixedSize(900, 600)
        self.btn1=QPushButton('공지 확인', self) #첫 매개변수는 버튼에 들어갈 문구, 두 번째 매개변수는 나 자신에게 버튼 추가한다.
        self.btn1.resize(self.btn1.sizeHint()) #resize는 버튼 사이즈 조절함수 sizeHint는 버튼 문구에 적당한 크기 반환해주느 함수
        self.btn1.move(20, 30) #버튼 왼쪽에서 20, 위쪽에서 30 이동
        self.setWindowTitle("Dalbits") #창 제목 설정하는 함수
        self.btn1.clicked.connect(v.ex2_showed)
        #self.btn2=QPushButton('스케줄러', self)
        #self.btn2.resize(self.btn1.sizeHint())
        #self.btn2.move(20, 60)
        #self.btn2.clicked.connect()

    def ex1_showed(self):
        self.show()



class Exam2(QWidget):
    def __init__(self):
        super().__init__() #부모 클래스의 init 함수 실행
        self.initUI() #여러가지를 생성하고 설정하는 함수
    def initUI(self):
        self.setWindowTitle("check_an") #창 제목 설정하는 함수
    def ex2_showed(self):
        flag, show_list = check_an.gosasapar(z.user_id, z.user_pw)
        if flag==0:
            ans = QMessageBox.question(self, "Login_error", "id, pw를 다시 입력해주세요.")
            sys.exit(0)

        if not show_list: #새로 올라온 공지 없을 경우
            lb = QLabel("There is no new announcement") #새로 올라온 공지 없다고 출력
            lb.move(50, 50)
            self.show()

        else:
            hbox = QVBoxLayout(self)
            for i in range(0, len(show_list)):
                lb = QLabel(show_list[i], self)
                hbox.addWidget(lb)
            self.setLayout(hbox)
            self.show()

    def keyPressEvent(self, e): #오버라이딩, e에는 눌린 키의 정보가 담김
        if e.key() == Qt.Key_Escape: #Qt.Key_Escape는 esc 키를 뜻하는 상수 그래서 esc 눌린다면
            self.close() #창을 닫는다


class login(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        log_lb = QLabel(self)
        pixmap = QPixmap('login.png')
        log_lb.setPixmap(pixmap)

        self.btn = QPushButton('Login', self)
        self.btn.move(260, 340)
        self.btn.clicked.connect(self.send)

        self.id = QLineEdit(self)
        self.id.resize(300, 32)
        self.id.move(170, 200)
        self.id.setStyleSheet("""QLineEdit { background-color: black; color: white }""")
        font = QFont("Times", 17, QFont.Bold)
        self.id.setFont(font)
        self.pw = QLineEdit(self)
        self.pw.setEchoMode(QLineEdit.Password)
        self.pw.resize(300, 32)
        self.pw.move(170, 265)
        self.pw.setStyleSheet("""QLineEdit { background-color: black; color: white }""")
        font = QFont("Times", 14, QFont.Bold)
        self.pw.setFont(font)

        self.setFixedSize(600, 400)
        self.setWindowTitle('Dalbits_Login')
        self.show()

    def send(self): #버튼 눌리면
        self.user_id = str(self.id.text()) #정보 전송후
        self.user_pw = str(self.pw.text())
        # if log_ck(self.user_id, self.user_pw) == True:
        #     w.ex1_showed()
        #     self.close() #창을 닫는다
        # else
        #     h.showed()

    def keyPressEvent(self, e): #오버라이딩, e에는 눌린 키의 정보가 담김
        if e.key() == Qt.Key_Return: #Qt.Key_Return는 enter 키를 뜻하는 상수 그래서 enter 눌린다면
            self.user_id = str(self.id.text()) #정보 전송후
            self.user_pw = str(self.pw.text())
            w.ex1_showed()
            self.close() #창을 닫는다

class log_window(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        er_lb=QLabel(self)
        er_lb.setPixmap(QPixmap("logerror.png"))
    def showed(self):
        self.show()
    def keyPressEvent(self, e): #오버라이딩, e에는 눌린 키의 정보가 담김
        if e.key() == Qt.Key_Escape: #Qt.Key_Escape는 esc 키를 뜻하는 상수 그래서 esc 눌린다면
            self.close() #창을 닫는다

app = QApplication(sys.argv) #필수적으로 쓰는 부분 그런가보다 하고 넘어가면 될 듯?
v = Exam2() #객체 생성
w = Exam1() #객체 생성
h = log_window()
z = login() #객체 생성

sys.exit(app.exec_()) #app.exec_()에서 메인 loop 계속 돌다가 창을 끄거나 하면 sys.exit로 프로그램 종료