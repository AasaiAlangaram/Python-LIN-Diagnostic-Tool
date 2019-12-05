from PyQt5.QtWidgets import *
import sys
import os
class Dialog(QWidget):
    def __init__(self):
        dn = os.path.dirname(os.path.realpath(__file__))
        print(dn)
        fn = open
        fp = open(dn + "/LIN_Fault_Data.txt","w+")
        fp.write('aasai')
        print('file opened')
        QWidget.__init__(self)
        layout = QGridLayout()
        self.setLayout(layout)
        label = QLabel("This is a dialog.")
        layout.addWidget(label, 0, 0)
        buttonbox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        layout.addWidget(buttonbox)
app = QApplication(sys.argv)
screen = Dialog()
screen.show()

sys.exit(app.exec_())
