from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys


class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        layout = QGridLayout()
        self.setLayout(layout)
        time = QTime()
        time.setHMS(13, 15, 40)
        timeedit = QTimeEdit()
        timeedit.setTime(time)
        layout.addWidget(timeedit, 0, 0)
app = QApplication(sys.argv)
screen = Window()
screen.show()
sys.exit(app.exec_())
Download: TimeEdit