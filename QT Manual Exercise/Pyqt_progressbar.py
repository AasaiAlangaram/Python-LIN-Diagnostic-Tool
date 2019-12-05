
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys

class Window(QWidget):

    def __init__(self):

        QWidget.__init__(self)
        layout = QGridLayout()
        self.setLayout(layout)

        progressbar = QProgressBar()
        progressbar.setMinimum(0)
        progressbar.setMaximum(100)
        progressbar.setOrientation(Qt.Horizontal)
        progressbar.setFormat("%p")
        progressbar.setTextVisible(True)

        layout.addWidget(progressbar,0,1)

app = QApplication(sys.argv)
screen = Window()
screen.show()
sys.exit(app.exec_())

