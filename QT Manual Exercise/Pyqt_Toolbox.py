from PyQt5.QtWidgets import *
import sys
class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        layout = QGridLayout()
        self.setLayout(layout)
        toolbox = QToolBox()

        label = QLabel()
        toolbox.addItem(label, "Hyundai")
        layout.addWidget(toolbox, 0, 0)
        label = QLabel()
        toolbox.addItem(label, "Toyota")
        layout.addWidget(toolbox, 1, 0)
        label = QLabel()
        toolbox.addItem(label, "Mercedes")
        layout.addWidget(toolbox, 2, 0)
app = QApplication(sys.argv)
screen = Window()
screen.show()
sys.exit(app.exec_())