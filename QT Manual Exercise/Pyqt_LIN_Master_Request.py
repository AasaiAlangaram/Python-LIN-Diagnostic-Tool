from PyQt5.QtWidgets import *
import sys


class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("LIN Messages")
        self.setGeometry(200, 200, 500, 300)
        self.setFixedSize(820, 320)
        self.show()
        self.NAD()

    def NAD(self):
        layout = QGridLayout()
        self.setLayout(layout)

        groupbox= QGroupBox("LIN Master frame Request (0X3C)")  # groupbox = QGroupBox(title)
        # groupbox.setCheckable(True)#his permits all child CheckBox or RadioButton widgets to be made sensitive or insenstive
        layout.addWidget(groupbox)

        # QHBoxLayout and QVBoxLayout classes that line up widgets horizontally and vertically.
        Hbox = QHBoxLayout()
        groupbox.setLayout(Hbox)

        self.lineedit=QLineEdit()
        Hbox.addWidget(self.lineedit)

        self.lineedit1 = QLineEdit()
        Hbox.addWidget(self.lineedit1)

        self.lineedit2 = QLineEdit()
        Hbox.addWidget(self.lineedit2)

        self.lineedit3 = QLineEdit()
        Hbox.addWidget(self.lineedit3)

        self.lineedit4= QLineEdit()
        Hbox.addWidget(self.lineedit4)

        self.lineedit5 = QLineEdit()
        Hbox.addWidget(self.lineedit5)

        self.lineedit6 = QLineEdit()
        Hbox.addWidget(self.lineedit6)

        self.lineedit7 = QLineEdit()
        Hbox.addWidget(self.lineedit7)

        button=QPushButton("Send")
        button.setToolTip("If you click this it will close this Window ")
        button.clicked.connect(self.send_msg)
        Hbox.addWidget(button)


        button = QPushButton("Exit")
        button.setToolTip("If you click this it will close this Window ")
        button.clicked.connect(self.exit_from_app)
        # button.setFlat(True)
        layout.addWidget(button, 1, 0)





    def exit_from_app(self):
        print("you clicked Exit Button\nIf you want to run again please press F5!@#")
        self.close()

    def return_pressed(self):
        print("His name is:", self.lineedit1.text())

    def send_msg(self):
        print(self.lineedit.text(),"",self.lineedit1.text(),"",self.lineedit2.text(),"",self.lineedit3.text(),"",self.lineedit4.text(),"",self.lineedit5.text(),"",self.lineedit6.text(),"",self.lineedit7.text())


app = QApplication(sys.argv)

screen = Window()
screen.show()

sys.exit(app.exec_())