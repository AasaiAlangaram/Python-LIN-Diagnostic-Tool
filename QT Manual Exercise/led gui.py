import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
import threading

import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(0)

GPIO.setup(12,GPIO.OUT)

class TesterThread(threading.Thread):
    def __init__(self, flag1):
        threading.Thread.__init__(self)
        self.flag  =0
        self.flag1 = flag1
        
        
    def run(self):
                
        while True:
            if self.flag1 == 0:
                print(self.flag1)
                GPIO.output(12,self.flag)
                #print(self.flag)
                sleep(1)
                self.flag ^=255
            
            
    def changeFlag(self, flag):
        self.flag1 = flag

class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        layout = QGridLayout()
        self.contorl =0
        
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
        
        self.button = QPushButton("LED Blink")
        self.button.clicked.connect(self.blink_clicked)
        setFnt = QFont("Times", 14, QFont.Bold)
        self.button.setFont(setFnt)
        self.button.setFixedSize(300, 30)
        self.button.move(20, 20)
        layout.addWidget(self.button)
        
        self.t = TesterThread(self.contorl)
        self.t.start()


    def on_button_clicked(self):
        print("LED ON")
        self.t.changeFlag(1)
        #print(self.control)
        GPIO.output(12, 1)

    def off_button_clicked(self):
        print("LED OFF")
        self.t.changeFlag(1)
        GPIO.output(12, 0)

    def blink_clicked(self):
        self.t.changeFlag(0)
        print("LED Blink's")

    
        '''
        while 1:
            GPIO.output(12,1)
            sleep(1)
            GPIO.output(12,0)
            sleep(1)
        '''
    
app = QApplication(sys.argv)
screen = Window()
screen.show()
sys.exit(app.exec_())
