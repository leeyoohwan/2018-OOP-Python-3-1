from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import *

class MainGUI(QWidget):
    def __init__(self):
        super().__init__()
        vbox = QVBoxLayout()
        hbox4 = QHBoxLayout()
        self.cal = QCalendarWidget(self)
        self.cal.setVerticalHeaderFormat(0)
        self.cal.setFixedSize(self.cal.sizeHint())
        hbox4. addWidget(self.cal)
        hbox4.addStretch()
        vbox.addLayout(hbox4)

        self.qtxt = QTextEdit(self)
        vbox.addWidget(self.qtxt)

        self.setLayout(vbox)

class MyMain(MainGUI):
    def __init__(self):
        super().__init__()

        self.cal.selectionChanged.connect(self.__cal_selectionchanged)

    def __cal_selectionchanged(self):
        self.qtxt.append("______ calendar")
        ddate = self.cal.selectedDate()
        self.qtxt.append(str(ddate.toPyDate()))

import sys
app = QApplication(sys.argv)
myWindow = MyMain()

myWindow.show()
app.exec_()