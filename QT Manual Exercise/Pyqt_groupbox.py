from PyQt5.QtWidgets import *
import sys

class GroupBox(QWidget):
    def __init__(self):
        
        QWidget.__init__(self)
        self.setWindowTitle("GroupBox")

        layout = QGridLayout()
        self.setLayout(layout)
        
        groupbox = QGroupBox("GroupBox Example")#groupbox = QGroupBox(title)
        #groupbox.setCheckable(True)#his permits all child CheckBox or RadioButton widgets to be made sensitive or insenstive
        layout.addWidget(groupbox)

        #QHBoxLayout and QVBoxLayout classes that line up widgets horizontally and vertically.
        vbox = QVBoxLayout()
        groupbox.setLayout(vbox)
        
        radiobutton = QRadioButton("RadioButton 1")
        #radiobutton.setChecked(True)
        vbox.addWidget(radiobutton)
        radiobutton = QRadioButton("RadioButton 2")
        vbox.addWidget(radiobutton)
        radiobutton = QRadioButton("RadioButton 3")
        vbox.addWidget(radiobutton)
        radiobutton = QRadioButton("RadioButton 4")
        vbox.addWidget(radiobutton)

        #Window size modify function
        self.setWindowTitle("!!!Aasai Application!!!")
        self.setGeometry(200,200,500,300)
        self.setFixedSize(820,320)
        self.show()
        
app = QApplication(sys.argv)

screen = GroupBox()
screen.show()

sys.exit(app.exec_())
