#https://www.youtube.com/channel/UCFinQvpLueFGR431gRsltOQ 참고하여 코드 작성

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap, QFont
import check_an
from login_check import *
from PyQt5.QtCore import Qt, QSize, QDate
import menu

calender=[]
day = []
schh = []

class MainWindow(QWidget):
    global v
    def __init__(self):
        super().__init__() #부모 클래스의 init 함수 실행
        self.initUI() #여러가지를 생성하고 설정하는 함수
    def initUI(self):
        label = QLabel(self) #배경 사진 지정
        pixmap = QPixmap('back.png')
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
        self.btn2.clicked.connect(g.show)

        self.btn3 = QPushButton('', self)
        self.btn3.setIcon(QIcon("bt2.png"))
        self.btn3.setIconSize(QSize(210, 70))
        self.btn3.resize(210, 70)
        self.btn3.move(550, 470)
        self.btn3.clicked.connect(m.menu_showed)

class Exam2(QWidget):
    def __init__(self):
        super().__init__() #부모 클래스의 init 함수 실행
    def ex2_showed(self):
        super().__init__()  # 부모 클래스의 init 함수 실행
        self.setWindowTitle("check_an") #창 제목 설정하는 함수
        show_list = check_an.gosasapar(z.user_id, z.user_pw)

        if not show_list: #새로 올라온 공지 없을 경우
            lb = QLabel("There is no new announcement") #새로 올라온 공지 없다고 출력
            lb.move(50, 50)
            self.show()

        else:
            self.hbox = QVBoxLayout(self)
            for i in range(0, len(show_list)):
                lb = QLabel(show_list[i], self)
                self.hbox.addWidget(lb)
            self.setLayout(self.hbox)
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
             w.show()
             self.close() #창을 닫는다
        else:
             h.showed()

    def keyPressEvent(self, e): #오버라이딩, e에는 눌린 키의 정보가 담김
        if e.key() == Qt.Key_Return: #Qt.Key_Return는 enter 키를 뜻하는 상수 그래서 enter 눌린다면
            self.user_id = str(self.id.text()) #정보 전송후
            self.user_pw = str(self.pw.text())
            if log_ck(self.user_id, self.user_pw) == 1:
                w.show()
                self.close() #창을 닫는다
            else :
                h.showed()

class menu_window(QWidget):
    def __init__(self):
        super().__init__()
    def menu_showed(self):
        br_menu, lu_menu, di_menu = menu.check_menu(z.user_id, z.user_pw)
        print(br_menu)
        print(lu_menu)
        print(di_menu)
        brbox = QVBoxLayout()
        lb = QLabel('아침')
        brbox.addWidget(lb)

        lubox = QVBoxLayout()
        lb = QLabel('점심')
        lubox.addWidget(lb)

        dibox = QVBoxLayout()
        lb = QLabel('저녁')
        dibox.addWidget(lb)

        for i in range(0, len(br_menu)):
            lb = QLabel(br_menu[i])
            brbox.addWidget(lb)
        # print("크앙!")
        for i in range(0, len(lu_menu)):
            lb = QLabel(lu_menu[i])
            lubox.addWidget(lb)
        # print("크앙!")
        for i in range(0, len(di_menu)):
            lb = QLabel(di_menu[i])
            dibox.addWidget(lb)

        self.hbox = QHBoxLayout(self)
        print("크앙!")
        self.hbox.addLayout(brbox)
        self.hbox.addLayout(lubox)
        self.hbox.addLayout(dibox)

        self.setLayout(self.hbox)
        self.show()

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
        sc_bt2.clicked.connect(a.show)
        sc_bt3=QPushButton('일정삭제', self)
        sc_bt3.resize(sc_bt3.sizeHint())
        sc_bt3.move(30, 230)
        sc_bt3.clicked.connect(b.initUI)

class schedule_add(QWidget):
    def __init__(self):
        vbox = QVBoxLayout()
        super().__init__()
        self.cal = QCalendarWidget(self)
        self.cal.setFixedSize(self.cal.sizeHint())
        self.cal.selectionChanged.connect(self.dayset)
        self.content_send=QPushButton("일정추가", self)
        self.content=QLineEdit(self)
        vbox.addWidget(self.cal)
        vbox.addWidget(self.content)
        vbox.addWidget(self.content_send)
        self.setLayout(vbox)
        self.set_day = str(QDate.currentDate().toPyDate()).split('-')
        self.content_send.clicked.connect(self.add_sch)

    def dayset(self):
        ddate = str(self.cal.selectedDate().toPyDate())
        self.set_day = ddate.split('-')

    def add_sch(self):
        global day
        global schh
        sch_day=int(self.set_day[0]+self.set_day[1]+self.set_day[2])
        print(sch_day)
        print(day)
        day.append(sch_day)
        schh.append(str(self.content.text()))
        sorter()

    def closeEvent(self, QCloseEvent):
        reset()

class schedule_del(QWidget):
    def __init__(self):
        super().__init__()

    def initUI(self):
        super().__init__()
        global day
        global schh
        self.setGeometry(800, 200, 300, 300)
        self.checkbox = []
        vbox=QVBoxLayout()
        for i in range(0, len(day)):
            self.checkbox.append(QCheckBox(str(day[i]) + "-" + schh[i], self))
            self.checkbox[i].resize(150, 30)
            vbox.addWidget(self.checkbox[i])

        self.dele = QPushButton('선택된 항목 삭제', self)
        self.dele.resize(self.dele.sizeHint())
        self.dele.clicked.connect(self.checkdelete)
        vbox.addWidget(self.dele)
        self.setLayout(vbox)
        self.show()

    def checkdelete(self):
        delday=[]
        delschh=[]
        for i in range(0, len(day)):
            if self.checkbox[i].isChecked() == True:
                delday.append(day[i])
                delschh.append(schh[i])

        for i in range(0, len(delday)):
            day.remove(delday[i])
            schh.remove(delschh[i])
        reset()
        self.close()


class schedule_check(QWidget):
    def __init__(self):
        super().__init__()
        fileopen()

    def show_sc(self):
        super().__init__()
        self.setFixedSize(200, 300)
        for i in range(0, len(day)):
            daylabel=QLabel(str(day[i]), self)
            schhlabel=QLabel(schh[i], self)
            daylabel.move(10, i*40)
            schhlabel.move(10, i*40+15)
        self.show()

def fileopen():  # 파일 오픈하여 캘린더에 담기. 처음 한번만 시행.
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
        day.append(int(spline[0]))
        schh.append(spline[1])
    f.close()

def sorter(): # 캘린더 리스트를 정렬합니다. v 값 기준.
    global day
    global schh
    for i in range(0, len(day)-1):
        minj = i
        for j in range(i, len(day)):
            if day[j] < day[minj]:
                tp = day[minj]
                day[minj]=day[j]
                day[j]=tp
                tp=schh[minj]
                schh[minj]=schh[j]
                schh[j]=tp
                minj = j
    print(day)
    print(schh)

def reset(): # 파일을 리셋합니다. 프로그램을 종료할 때 시행합니다
    f = open('schedule.txt', 'w')
    f.write('')
    f.close()
    f = open('schedule.txt', 'a')
    for i in range(0, len(day)):
        f.write(str(day[i]) + "/" + schh[i] +"\n")
    f.close()


app = QApplication(sys.argv) #필수적으로 쓰는 부분 그런가보다 하고 넘어가면 될 듯?
v = Exam2() #객체 생성
a = schedule_add()
f = schedule_check()
b = schedule_del()
g = schedule_window()
m = menu_window()
w = MainWindow() #객체 생성
h = log_window()
z = login() #객체 생성

sys.exit(app.exec_()) #app.exec_()에서 메인 loop 계속 돌다가 창을 끄거나 하면 sys.exit로 프로그램 종료