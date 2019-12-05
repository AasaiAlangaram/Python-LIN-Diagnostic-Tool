from PyQt5.QtWidgets import *
import sys
class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        layout = QGridLayout()
        self.setLayout(layout)
        self.lineedit = QLineEdit()
        self.lineedit.returnPressed.connect(self.return_pressed)
        layout.addWidget(self.lineedit, 0, 0)
    def return_pressed(self):
        print(self.lineedit.text())
app = QApplication(sys.argv)
screen = Window()
screen.show()
sys.exit(app.exec_())
