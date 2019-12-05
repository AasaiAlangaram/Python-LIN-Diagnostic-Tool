from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

import sys

class Tab(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        layout = QGridLayout()
        self.setLayout(layout)

        self.setWindowTitle("SL Diagnostic GUI")
        self.setGeometry(200, 200, 800, 800)
        self.setFixedSize(820, 820)
        self.show()

        tabwidget = QTabBar()
        tabwidget.addTab("LIN Message")
        layout.addWidget(tabwidget)

        groupbox1 = QGroupBox("NAD")
        layout.addWidget(groupbox1)

        groupbox1=QLabel("NAD Type")
        layout.addWidget(groupbox1,0,0)


        groupbox = QGroupBox("LIN Master frame Request (0X3C)")
        layout.addWidget(groupbox)

        Hbox = QHBoxLayout()
        groupbox.setLayout(Hbox)

        self.lineedit = QLineEdit()
        Hbox.addWidget(self.lineedit)

        self.lineedit1 = QLineEdit()
        Hbox.addWidget(self.lineedit1)

        self.lineedit2 = QLineEdit()
        Hbox.addWidget(self.lineedit2)

        self.lineedit3 = QLineEdit()
        Hbox.addWidget(self.lineedit3)

        self.lineedit4 = QLineEdit()
        Hbox.addWidget(self.lineedit4)

        self.lineedit5 = QLineEdit()
        Hbox.addWidget(self.lineedit5)

        self.lineedit6 = QLineEdit()
        Hbox.addWidget(self.lineedit6)

        self.lineedit7 = QLineEdit()
        Hbox.addWidget(self.lineedit7)

        button = QPushButton("Send")
        button.setToolTip("Click this button to send this message")
        button.clicked.connect(self.send_msg)
        Hbox.addWidget(button)



    def send_msg(self):
            print(self.lineedit.text(), "", self.lineedit1.text(), "", self.lineedit2.text(), "", self.lineedit3.text(),
                  "", self.lineedit4.text(), "", self.lineedit5.text(), "", self.lineedit6.text(), "",
                  self.lineedit7.text())


app = QApplication(sys.argv)
screen = Tab()
screen.show()
sys.exit(app.exec_())
