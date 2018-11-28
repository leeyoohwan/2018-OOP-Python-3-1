# 스케쥴러 코드 :: 작성자 배상우
# 스케쥴러는 파일입출력을 통한 정보저장 기능이 필요합니다. 곧 보완하겠습니다.
import time,  os, sys

class sch : # 스케쥴 클래스. 그냥 구조체 개념입니다.
    def __init__(self, y, m, d, c): # 클래스 호출될 때마다 안에 변수를 담습니다.
        self.year = y 
        self.month = m
        self.day = d
        self.contents = c
        self.v = y*10000 + m*100 + d # 시간 계산에 사용하기 위한 꼼수 값입니다.
calender = [] # 스케쥴 클래스를 담는 리스트입니다. 항상 시간순으로 정렬됩니다.

# calender = file open txt

message = "노력하는 자만이 기회를 잡을 수 있다"


def sorter(): # 캘린더 리스트를 정렬합니다. value 값 기준.
    b = 3+1


def printer(): # 캘린더 리스트를 출력하는 함수입니다.
    print("")
    print(message)
    for i in calender:
        print("─" * 30)
        print(str(i.year) + "년 " + str(i.month) + "월 " + str(i.day) + "일 ::")
        print(i.contents)
  

def addr(): # 스케쥴을 입력받습니다. 연도, 달, 날짜는 숫자고 내용만 문장입니다.
    y = int(input("연도를 입력해 주세요 : ")) # 올해보다 작은 연도를 입력하면 예외처리
    m = int(input("월을 입력해 주세요 : ")) # 1~12 이외의 수를 입력하면 예외처리
    d = int(input("날짜를 입력해 주세요 : ")) # m에 따라 예외처리
    c = input("내용을 입력해 주세요 : ")
    calender.append(sch(y, m, d, c)) # 캘린더에 추가합니다.

def eraser(): # 인덱스 받아서 스케쥴을 지웁니다
    index = int(input("지울 스케쥴을 선택해 주세요 : "))
    calender.pop(index-1)


# def checker(): # 이미 날짜가 지난 스케쥴을 지웁니다. value 값 기준.
#    print("")

def writer(): # 유저 지정 문구를 수정합니다.
    global message
    message = input("수정할 문장 : ")


######################################## 실제 프로그램 작동 시작 지점입니다. GUI에선 의미없는 파트.
while True: # 사용자의 행동을 기다립니다.
    os.system('cls')
    # checker()
    # sorter()
    printer()
    print("─" * 30)
    print("")
    print("1: 추가 / 2: 삭제 / 3: 문구 / 0: 종료")
    do = int(input("무엇을 하시겠습니까? : "))
    os.system('cls')
    if do == 1:
        addr()
    elif do == 2:
        eraser()
    elif do == 3:
        writer()
    elif do == 0:
        sys.exit()
    else:
        print("잘못된 입력입니다.")
