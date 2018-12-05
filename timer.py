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



# 경다녕 : 공부한 시간 측정해서 그래프로 그리는 프로그램

# matplotlib를 통해 그래프를 플롯 창에 띄우는데, 저장이 되는지는 모르겠음
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


