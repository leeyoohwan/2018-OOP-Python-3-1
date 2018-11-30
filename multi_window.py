#https://www.youtube.com/channel/UCFinQvpLueFGR431gRsltOQ 참고하여 코드 작성

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QVBoxLayout, QMessageBox
from PyQt5.QtGui import QIcon, QPixmap, QFont
import check_an
from login_check import *
from PyQt5.QtCore import Qt, QSize
# from Scheduler import *

calender=[]

class MainWindow(QWidget):
    global v
    def __init__(self):
        super().__init__() #부모 클래스의 init 함수 실행
        self.initUI() #여러가지를 생성하고 설정하는 함수
    def initUI(self):
        label = QLabel(self) #배경 사진 지정
        pixmap = QPixmap('background.png')
        label.setPixmap(pixmap)
        self.setFixedSize(900, 600)
        self.setWindowTitle("Dalbits")  # 창 제목 설정

        self.btn1=QPushButton('', self) #첫 매개변수는 버튼에 들어갈 문구, 두 번째 매개변수는 나 자신에게 버튼 추가한다.
        self.btn1.resize(210, 70) #resize는 버튼 사이즈 조절함수 sizeHint는 버튼 문구에 적당한 크기 반환해주는 함수
        self.btn1.setIcon(QIcon("bt1.png"))
        self.btn1.setIconSize(QSize(210, 70))
        self.btn1.move(550, 100) #버튼 왼쪽에서 20, 위쪽에서 30 이동
        self.btn1.clicked.connect(v.ex2_showed)

        self.btn2=QPushButton('', self)
        self.btn2.setIcon(QIcon("bt2.png"))
        self.btn2.setIconSize(QSize(210, 70))
        self.btn2.resize(210, 70)
        self.btn2.move(550, 250)
        self.btn2.clicked.connect(g.showed)

    def ex1_showed(self):
        self.show()


class Exam2(QWidget):
    def __init__(self):
        super().__init__() #부모 클래스의 init 함수 실행
        self.initUI() #여러가지를 생성하고 설정하는 함수
    def initUI(self):
        self.setWindowTitle("check_an") #창 제목 설정하는 함수
    def ex2_showed(self):
        show_list = check_an.gosasapar(z.user_id, z.user_pw)

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

        self.id = QLineEdit(self) #id 입력하는 줄
        self.id.resize(300, 32)
        self.id.move(170, 200)
        self.id.setStyleSheet("""QLineEdit { background-color: black; color: white }""")
        font = QFont("Times", 17, QFont.Bold)
        self.id.setFont(font)

        self.pw = QLineEdit(self) #pw 입력하는 줄
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
        if log_ck(self.user_id, self.user_pw) == 1:
             w.ex1_showed()
             self.close() #창을 닫는다
        else:
             h.showed()

    def keyPressEvent(self, e): #오버라이딩, e에는 눌린 키의 정보가 담김
        if e.key() == Qt.Key_Return: #Qt.Key_Return는 enter 키를 뜻하는 상수 그래서 enter 눌린다면
            self.user_id = str(self.id.text()) #정보 전송후
            self.user_pw = str(self.pw.text())
            if log_ck(self.user_id, self.user_pw) == 1:
                w.ex1_showed()
                self.close() #창을 닫는다
            else :
                h.showed()

class log_window(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        er_lb=QLabel(self)
        er_lb.setPixmap(QPixmap("logerror.png"))
        self.setFixedSize(400, 240)
    def showed(self):
        z.id.clear()
        z.pw.clear()
        self.show()
    def keyPressEvent(self, e): #오버라이딩, e에는 눌린 키의 정보가 담김
        if e.key() == Qt.Key_Escape: #Qt.Key_Escape는 esc 키를 뜻하는 상수 그래서 esc 눌린다면
            self.close() #창을 닫는다

class schedule_window(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setFixedSize(500, 500)
        sc_bt1=QPushButton('일정확인', self)
        sc_bt1.resize(sc_bt1.sizeHint())
        sc_bt1.move(30, 30)
        sc_bt1.clicked.connect(f.show_sc)
        sc_bt2=QPushButton('일정추가', self)
        sc_bt2.resize(sc_bt2.sizeHint())
        sc_bt2.move(30, 130)
        # sc_bt2.clicked.connect()
    def showed(self):
        self.show()

class addschedule_window(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setFixedSize(500, 500)



class schedule_check(QWidget):
    def __init__(self):
        super().__init__()

    def show_sc(self):
        self.setFixedSize(100, 300)
        fileopen()
        day, schh = printer()
        for i in range(0, len(day)):
            daylabel=QLabel(str(day[i]), self)
            schhlabel=QLabel(schh[i], self)
            daylabel.move(10, i*30)
            schhlabel.move(10, i*30+20)
        self.show()

def fileopen():  # 파일 오픈하여 캘린더에 담기. 처음 한번만 시행.
    global calender
    try:
        f = open("schedule.txt", 'r')
    except:
        print("스케줄러 파일이 감지되지 않았습니다")
        print("올바른 위치에 해당 프로그램이 있는지 확인해 주세요")
        print("문제가 없는데도 계속 오류가 발생할 시")
        print("배상우 학생에게 페이스북 메시지로 제보해주세요")
        sys.exit()

    while True:
        line = f.readline()
        if not line: break
        spline = line.split('/')
        spline[1] = spline[1].rstrip('\n')
        calender.append(int(spline[0]))
        calender.append(spline[1])
    f.close()

def printer():  # 캘린더 리스트를 출력하는 함수입니다.
    global calender
    day = []
    schh = []
    for i in range(0, len(calender)):
        if i%2==0:
            day.append(calender[i])
        else:
            schh.append(calender[i])
    print(day)
    print(schh)
    return day, schh



app = QApplication(sys.argv) #필수적으로 쓰는 부분 그런가보다 하고 넘어가면 될 듯?
v = Exam2() #객체 생성
f = schedule_check()
g = schedule_window()
w = MainWindow() #객체 생성
h = log_window()
z = login() #객체 생성

sys.exit(app.exec_()) #app.exec_()에서 메인 loop 계속 돌다가 창을 끄거나 하면 sys.exit로 프로그램 종료

