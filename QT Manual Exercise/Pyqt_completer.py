from PyQt5.QtWidgets import *
import sys
class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        layout = QGridLayout()
        self.setLayout(layout)
        names = ["George", "Marcus", "Samantha", "Steven", "Maria"]
        completer = QCompleter(names)
        self.lineedit = QLineEdit()
        self.lineedit.setCompleter(completer)
        layout.addWidget(self.lineedit, 0, 0)
app = QApplication(sys.argv)
screen = Window()
screen.show()
sys.exit(app.exec_())