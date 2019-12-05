from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
class Window(QWindow):
    def __init__(self):
        QWindow.__init__(self)
        self.setTitle("This is resized window")
        #self.resize(400, 300)
        self.setWidth(700)
        self.setHeight(450)

