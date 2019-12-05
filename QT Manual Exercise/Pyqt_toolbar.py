from PyQt5.QtWidgets import *
import sys
class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        layout = QGridLayout()
        self.setLayout(layout)
        toolbar = QToolBar()
        layout.addWidget(toolbar)
        toolbutton = QToolButton()
        toolbutton.setText("Button 1")
        toolbutton.setCheckable(True)
        toolbutton.setAutoExclusive(True)
        toolbar.addWidget(toolbutton)
        toolbutton = QToolButton()
        toolbutton.setText("Button 2")
        toolbutton.setCheckable(True)
        toolbutton.setAutoExclusive(True)
        toolbar.addWidget(toolbutton)
app = QApplication(sys.argv)
screen = Window()
screen.show()
sys.exit(app.exec_())