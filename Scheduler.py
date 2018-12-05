# 스케쥴러 코드 :: 작성자 배상우
# 체커와 솔터 구성 완료, 각종 예외처리 추가.
# 파일 입출력 제작 완료
# 랜덤 추천 제작 완료
import time,  os, sys, datetime
from random import *

now = datetime.datetime.now()
nowY = int(now.strftime('%Y'))
nowm = int(now.strftime('%m'))
nowd = int(now.strftime('%d'))
nowv = int(now.strftime('%Y'))*10000 + int(now.strftime('%m'))*100 + int(now.strftime('%d'))

class sch : # 스케쥴 클래스. 그냥 구조체 개념입니다.
    def __init__(self, c,  v): # 클래스 호출될 때마다 안에 변수를 담습니다.
        self.c = c
        self.v = v
calender = [] # 스케쥴 클래스를 담는 리스트입니다. 항상 시간순으로 정렬됩니다.

def value_calc(): # value 반환 함수
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
    return(value) # 반환

def open(): # 저장된 파일을 불러옵니다
    f = open("data.txt", 'r')
    lines = f.readlines()
    for line in lines:
        l = line.rtstrip('\n').split('/')
        calender.append(sch(l[0], int(l[1])))
    f.close()
open()

def reset(): # 파일을 리셋합니다. 프로그램을 종료할 때 시행합니다
    f = open('data.txt', 'w')
    f.write('')
    f.close()
    f = open('data.txt', 'a')
    for i in calender:
        f.write(i.c + "/" + str(i.v))
    f.close()

def sorter(): # 캘린더 리스트를 정렬합니다. v 값 기준.
    for i in range(0, len(calender)-1):
        minj = i
        for j in range(i, len(calender)):
            if calender[j].v < calender[minj].v:
                minj = j
            calender[minj], calender[i] = calender[i], calender[minj]

def printer(i): # 캘린더 리스트에서 환산된 value값과 내용을 출력합니다
    print(str(int(i.v/10000)) + "년 " + str(int((i.v%10000)/100)) + "월 " + str(int(i.v%100)) + "일 ::")
    print(i.c)

def layout(): # 전체 레이아웃입니다.
    os.system('cls')
    print("스케줄을 잘 지켜 성실한 사람으로 거듭납시다")
    for i in calender:
        print("─" * 30)
        printer(i)
    print("─" * 30)
    print("")
    print("1: 추가 / 2: 삭제 / 3: 랜덤 추천 / 0: 종료")
    do = int(input("무엇을 하시겠습니까? : "))
    os.system('cls')
    return (do)

def eraser(): # 인덱스 받아서 스케쥴을 지웁니다
    index = int(input("지울 스케쥴을 선택해 주세요 : "))
    if index >= 0 and index <= (len(calender)-1):
        calender.pop(index-1)

def checker(): # 이미 지난 스케줄을 체크합니다
    for i in range(0, len(calender)):
        if calender[i] < nowv:
            calender.pop(i)
            checked += 1
    return checked
checker()

def suggest(): # 사용자에게 랜덤으로 할 일을 출력합니다
    print("할 일을 랜덤으로 출력해 볼까요?")
    print("")
    s = randrange(len(calender)-1)
    s = calender[s]
    printer(s)
    print("")
    print("띠용~ 이 일을 해보는 게 어때요?")
    

######################################## 실제 프로그램 작동 시작 지점입니다. GUI에선 의미없는 파트.
while True: # 사용자의 행동을 기다립니다.
    sorter()
    do = layout()
    if do == 1:
        v = exclear()
        c = input("내용을 입력해 주세요 : ")
        calender.append(c, v)
    elif do == 2:
        eraser()
    elif do == 3:
        suggest()
    elif do == 0:
        reset()
        sys.exit()
    else:
        print("잘못된 입력입니다.")