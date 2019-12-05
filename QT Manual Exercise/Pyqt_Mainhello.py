from PyQt5.QtWidgets import *
import sys
import Pyqt_helloworld

class main(QWidget):

    def __init__(self):
        super().__init__(self)
        self.Window()
app=QApplication(sys.argv)
screen=main()
screen.show()
sys.exit(app.exec_())