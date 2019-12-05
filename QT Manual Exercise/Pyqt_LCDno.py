from PyQt5.QtWidgets import *
import sys

class Window(QWidget):

    def __init__(self):

        QWidget.__init__(self)
        layout = QGridLayout()
        self.setLayout(layout)
        lcdnumber = QLCDNumber()
        lcdnumber.display("AASAI")
        layout.addWidget(lcdnumber, 0, 0)

app = QApplication(sys.argv)
screen = Window()
screen.show()
sys.exit(app.exec_())