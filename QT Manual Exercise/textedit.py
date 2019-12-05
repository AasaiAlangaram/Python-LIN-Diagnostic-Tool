from PyQt5.QtWidgets import *
import sys
class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.list= [1]
        layout = QGridLayout()
        self.setLayout(layout)
        textedit = QTextBrowser()
        textedit.setPlaceholderText("This is some placeholder text.")
        textedit.setPlainText(self.list)
        layout.addWidget(textedit, 0, 0)
app = QApplication(sys.argv)
screen = Window()
screen.show()
sys.exit(app.exec_())