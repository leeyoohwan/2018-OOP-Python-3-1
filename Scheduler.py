# 스케쥴러 코드 :: 작성자 배상우
# 체커와 솔터가 구성 완료되었으며, 각종 예외처리도 추가했습니다.
# 스케쥴러는 파일입출력을 통한 정보저장 기능이 필요합니다. 곧 보완하겠습니다.
import time,  os, sys, datetime

now = datetime.datetime.now()
nowY = int(now.strftime('%Y'))
nowm = int(now.strftime('%m'))
nowd = int(now.strftime('%d'))
nowv = int(now.strftime('%Y'))*10000 + int(now.strftime('%m'))*100 + int(now.strftime('%d'))

class sch : # 스케쥴 클래스. 그냥 구조체 개념입니다.
    def __init__(self, c,  value): # 클래스 호출될 때마다 안에 변수를 담습니다.
        self.contents = c
        self.v = value
calender = [] # 스케쥴 클래스를 담는 리스트입니다. 항상 시간순으로 정렬됩니다.

# calender = file open txt

message = "노력하는 자만이 기회를 잡을 수 있다"


def sorter(): # 캘린더 리스트를 정렬합니다. v 값 기준.
    for i in range(0, len(calender)-1):
        minj = i
        for j in range(i, len(calender)):
            if calender[j].v < calender[minj].v:
                minj = j
            calender[minj], calender[i] = calender[i], calender[minj]


def printer(): # 캘린더 리스트를 출력하는 함수입니다.
    print("")
    print(message)
    for i in calender:
        print("─" * 30)
        print(str(int(i.v/10000)) + "년 " + str(int((i.v%10000)/100)) + "월 " + str(int(i.v%100)) + "일 ::")
        print(i.contents)
  
def addr(): # 스케쥴을 입력받습니다. 연도, 달, 날짜는 숫자고 내용만 문장입니다.
    while True:
        y = int(input("연도를 입력해 주세요 : ")) # 예외처리
        if y < nowY:
            print("올바른 연도를 입력해 주세요")
        else:
            break
    
    while True:
        m = int(input("월을 입력해 주세요 : ")) # v값에 따라 예외처리
        value = y*100 + m
        if value < nowY*100 + nowm:
            print("올바른 월을 입력해 주세요")
        else:
            break
    
    while True:
        d = int(input("날짜를 입력해 주세요 : ")) # v값에 따라 예외처리
        value = value*100 + d
        if value < nowv:
            print("올바른 날을 입력해 주세요")
        else:
            break

    c = input("내용을 입력해 주세요 : ")
    calender.append(sch(c, value)) # 캘린더에 추가합니다.

def eraser(): # 인덱스 받아서 스케쥴을 지웁니다
    index = int(input("지울 스케쥴을 선택해 주세요 : "))
    if index >= 0 and index <= (len(calender)-1):
        calender.pop(index-1)

def writer(): # 유저 지정 문구를 수정합니다.
    global message
    message = input("수정할 문장 : ")

def checker(): # 이미 지난 스케줄을 체크합니다
    checked = 0
    for i in range(0, len(calender)):
        if calender[i] < nowv:
            calender.pop(index)
            checked += 1
    return checked

######################################## 실제 프로그램 작동 시작 지점입니다. GUI에선 의미없는 파트.
while True: # 사용자의 행동을 기다립니다.
    #os.system('cls')
    ck = checker()
    if ck > 0:
        print(str(ck) + "개의 지난 스케줄이 지워졌습니다")
    sorter()
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
