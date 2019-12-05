from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys
class Window(QWidget):
    def __init__(self):

        QWidget.__init__(self)
        layout = QGridLayout()
        self.setLayout(layout)

        menubar = QMenuBar()
        layout.addWidget(menubar, 0, 0)
        actionFile = menubar.addMenu("File")
        actionFile.addAction("New")
        actionFile.addSeparator()
        actionFile.addAction("Open")
        actionFile.addSeparator()
        actionFile.addAction("Quit")
        menubar.addMenu("Edit")
        menubar.addMenu("View")
        menubar.addMenu("Help")

app = QApplication(sys.argv)
screen = Window()
screen.show()
sys.exit(app.exec_())