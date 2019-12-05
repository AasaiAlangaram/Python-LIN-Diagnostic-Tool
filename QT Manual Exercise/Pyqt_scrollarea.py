from PyQt5.QtWidgets import *
from PyQt5 import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        layout = QGridLayout()
        self.setLayout(layout)
        textedit = QTextEdit()
        textedit.setPlaceholderText("This is some placeholder text.")
        layout.addWidget(textedit, 0, 0)
        scrollbar = QScrollBar()
        scrollbar = QScrollBar(Qt.Vertical)
        layout.addWidget(scrollbar)

app = QApplication(sys.argv)
screen = Window()
screen.show()
sys.exit(app.exec_())