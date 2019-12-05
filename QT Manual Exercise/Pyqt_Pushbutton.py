from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
import sys
class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        layout = QGridLayout()
        self.setLayout(layout)
        self.setWindowTitle("!!!பிறந்த நாள் நல்வாழ்த்துக்கள்!!!")
        self.setGeometry(200, 200, 500, 300)
        self.setFixedSize(820, 320)
        self.show()
        self.button = QPushButton("Today Praveen Bday")
        self.button.clicked.connect(self.on_button_clicked)
        setFnt = QFont("Times", 14, QFont.Bold)
        self.button.setFont(setFnt)
        self.button.setFixedSize(300, 30)
        self.button.move(20, 20)
        layout.addWidget(self.button)
    def on_button_clicked(self):
            print("*****Wishing you a very happy birthday from Python.com\nMay your life filled with full of Happiness and joy\nNight party mudichitu Chicken vangitu vada(lol)****** ")
app = QApplication(sys.argv)
screen = Window()
screen.show()
sys.exit(app.exec_())
