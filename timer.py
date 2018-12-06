"""
import sys
import threading

cnt = 0


def start_timer(time):
    # 타이머 함수, 입력된 시간(초)이 지날때까지 초 카운트 해주다가 stop 출력
    global cnt
    cnt += 1
    print(cnt)

    timer = threading.Timer(1, start_timer, args=[time])
    timer.start()

    if cnt == time :
        print('stop')
        timer.cancel()


start_timer(5)

"""

"""
#!/usr/bin/env python3

# Display UTC.
# started with https://docs.python.org/3.4/library/tkinter.html#module-tkinter

import tkinter as tk
import time

def current_iso8601():
    #Get current date and time in ISO8601
    # https://en.wikipedia.org/wiki/ISO_8601
    # https://xkcd.com/1179/
    return time.strftime("%Y%m%d T %H%M%S Z", time.gmtime())

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.now = tk.StringVar()
        self.time = tk.Label(self, font=('Helvetica', 24))
        self.time.pack(side="top")
        self.time["textvariable"] = self.now

        self.QUIT = tk.Button(self, text="QUIT", fg="red",
                                            command=root.destroy)
        self.QUIT.pack(side="bottom")

        # initial time display
        self.onUpdate()

    def onUpdate(self):
        # update displayed time
        self.now.set(current_iso8601())
        # schedule timer to call myself after 1 second
        self.after(1000, self.onUpdate)

root = tk.Tk()
app = Application(master=root)
root.mainloop()

"""

"""
# 그래프 그리기 : matplotlib라는 라이브러리를 활용하여 그래프를 그릴 수 있음

import matplotlib.pyplot as plt

year = [0,1,2,3,4]
pop = [2,4,6,7,8]

plt.plot(year,pop)
plt.show()

"""


"""
# 경다녕 : 공부한 시간 측정해서 그래프로 그리는 프로그램

# matplotlib를 통해 그래프를 플롯 창에 띄우는데, 실행 폴더에 그래프를 이미지로 저장, 업뎃
# https://hashcode.co.kr/questions/3506/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EA%B7%B8%EB%9E%98%ED%94%84%EB%A5%BC-%EC%82%AC%EC%A7%84%EC%9C%BC%EB%A1%9C-%EC%A0%80%EC%9E%A5%ED%95%98%EB%A0%A4%EA%B3%A0-%ED%95%98%EB%8A%94%EB%8D%B0-%EC%95%88%EB%90%98%EC%9A%94
# 위 링크 참고
import matplotlib.pyplot as plt
import tkinter as tk
import time
import sys

# 현재 시각을 튜플로 저장
current_time = time.localtime()
# print(current_time)

# 앞으로 매일 공부한 양을 체크, 기록할 파일.
# 날짜와 공부 시작시간, 끝난 시간, delta t 값이 저장된다
f1 = open("dataSave.txt", 'w')
f1.write(str(current_time[0]) + ' ' + str(current_time[1]) + ' ' + str(current_time[2]))
f1.write('\n')
f1.write(str(current_time[3]) + ' ' + str(current_time[4]) + ' ' + str(current_time[5]))

time.sleep(3)

current_time = time.localtime()
f1.write('\n')
f1.write(str(current_time[3]) + ' ' + str(current_time[4]) + ' ' + str(current_time[5]))
f1.close()

f2 = open("dataSave.txt", 'r')
print(f2.read())
# 시간 저장이 되는지 확인

"""


import matplotlib.pyplot as plt
import tkinter as tk
import time
import sys

# 구현기능
# 공부 시작, 끝 시간 입력, 기록하는 스톱워치 기능
# 날짜별 누적 공부 시간 걔산
# 날짜별 누적 공부 시간 그래프로 그려 파일로 저장, 같은 이름에 업데이트 계속
#



# 사용자가 공부 시작 직전에 눌러 시간 측정을 시작함
startCheck = input("Enter anything to start Studying")
# 시작 시각을 튜플로 저장
starting_time = time.localtime()
# print(starting_time)
today = str(starting_time[0])+' '+str(starting_time[1])+' '+str(starting_time[2])

# 사용자가 공부를 끝내고 눌러 시간 측정 끝냄
endCheck = input("Enter anything to end Studying")
# 끝 시각도 저장
ending_time = time.localtime()

# delta t, 즉 공부한 시간 계산하고 저장
delta_time = []
for i in range(3,6):
    delta_time.append(str(ending_time[i]-starting_time[i]))





# 앞으로 매일 공부한 양을 체크, 기록할 파일.
# 이전에 적혀있던 내용 save
f = open('dataSave.txt', 'r')
lines = f.readlines()  # 모든 라인을 읽어 리스트로 저장
f.close()

lines.reverse()  # 읽은 라인을 역순으로 정렬--> 최신 것에 접근하려고
# 가장 최근에 저장된 날짜가 오늘과 같으면 newchk:False, 있는거에 누적시키고
# 그렇지 않으면 newchk:True, 새로 날짜 파서 공부한 시간 저장할거임
if not lines:
    lastDay = 'EMPTY'
else:
    lastDay = lines[1]
newchk = True
if lastDay == today:
    newchk = False


if newchk == True:
    # 그날 날짜와 누적 delta t 값이 차례로 저장된다
    f = open("dataSave.txt", 'a')
    f.write(today)
    f.write('\n')
    f.write(delta_time[0]+' '+delta_time[1]+' '+delta_time[2])
    f.close()
else:
    # 지난 번 값을 불러와서 더한 다음 다시 저장
    lastStudy = rlines[0].split()
    for i in range(0,3):
        delta_time[i] = str(int(lastStudy[i])+int(delta_time[i]))
    lines[0] = delta_time[0]+' '+delta_time[1]+' '+delta_time[2]+'\n'
    lines.reverse()
    f = open("dataSave.txt",w)
    for line in lines:
        f.write(line)
    f.close()






