import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont

import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(0)

GPIO.setup(12,GPIO.OUT)

class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        layout = QGridLayout()
        self.setLayout(layout)
        self.setWindowTitle("LED TEST GUI")
        self.setGeometry(200, 200, 500, 300)
        self.setFixedSize(820, 320)
        self.show()

        self.button = QPushButton("LED ON")
        self.button.clicked.connect(self.on_button_clicked)
        setFnt = QFont("Times", 14, QFont.Bold)
        self.button.setFont(setFnt)
        self.button.setFixedSize(300, 30)
        self.button.move(20, 20)
        layout.addWidget(self.button)

        self.button = QPushButton("LED OFF")
        self.button.clicked.connect(self.off_button_clicked)
        setFnt = QFont("Times", 14, QFont.Bold)
        self.button.setFont(setFnt)
        self.button.setFixedSize(300, 30)
        self.button.move(20, 20)
        layout.addWidget(self.button)

    def on_button_clicked(self):
        print("LED ON")
        GPIO.output(12, 1)

    def off_button_clicked(self):
        print("LED OFF")
        GPIO.output(12, 0)

app = QApplication(sys.argv)
screen = Window()
screen.show()
sys.exit(app.exec_())