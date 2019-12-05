from PyQt5.QtWidgets import *
import sys
class Dialog(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        layout = QGridLayout()
        spalsh=QSplashScreen()
        splash.show()
app = QApplication(sys.argv)
screen = Dialog()
screen.show()

sys.exit(app.exec_())