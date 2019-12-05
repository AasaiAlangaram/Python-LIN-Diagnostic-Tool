from PyQt5.QtWidgets import *
import sys
class MessageBox(QMessageBox):
    def __init__(self):
        QMessageBox.__init__(self)
        self.setText("This is a MessageBox, typically used to convey short messages to the user.")
        self.setInformativeText("Informative text provides more space to explain the message purpose.")
        self.setIcon(QMessageBox.Information)
        self.setStandardButtons(QMessageBox.Close)

app = QApplication(sys.argv)
screen = MessageBox()
screen.show()
sys.exit(app.exec_())