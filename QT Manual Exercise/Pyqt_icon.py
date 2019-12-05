from PyQt5.QtWidgets import *
import sys

class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.setgeometry(50,50,500,300)
        self.setWindowTitle("ICON")
        self.show()

app = QApplication(sys.argv)
screen = Window()
screen.show()
sys.exit(app.exec_())