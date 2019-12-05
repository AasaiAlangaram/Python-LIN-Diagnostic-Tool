'''WORKING
from PyQt5.QtWidgets import *
import sys
class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("window")
        layout = QGridLayout()
        self.setLayout(layout)
        label = QLabel("Hello, World!")
        layout.addWidget(label, 0, 0)
app = QApplication(sys.argv)
screen = Window()
screen.show()
sys.exit(app.exec_())'''
#not working
from PyQt5.QtWidgets import *
import sys
class Window(QWidget):
    def __init__(self):
        super(Window,self).__init__(self)
        self.setWindowTitle("window")

app = QApplication(sys.argv)
screen =Window()
screen.show()
sys.exit(app.exec_())