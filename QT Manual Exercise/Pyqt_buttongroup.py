from PyQt5.QtWidgets import *
import sys

class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        layout = QGridLayout()
        self.setLayout(layout)
        self.buttongroup = QButtonGroup()

        #Window size modify function
        self.setWindowTitle("!!!Aasai Application!!!")
        self.setGeometry(200,200,500,300)
        self.setFixedSize(820,320)
        self.show()
        
        #To enforce that only one button in the group can be selected at a time
        self.buttongroup.setExclusive(False)
        self.buttongroup.buttonClicked[int].connect(self.on_button_clicked)

        button = QPushButton("Button 1")
        self.buttongroup.addButton(button, 1)#buttongroup.addButton(button, id)
        layout.addWidget(button,0,0)
        
        button = QPushButton("Button 2")
        self.buttongroup.addButton(button, 2)##buttongroup.addButton(button, id)
        layout.addWidget(button,0,1)

        button = QPushButton("Button 3")
        self.buttongroup.addButton(button, 3)#buttongroup.addButton(button, id)
        layout.addWidget(button,1,0)
        
        button = QPushButton("Button 4")
        self.buttongroup.addButton(button, 4)##buttongroup.addButton(button, id)
        layout.addWidget(button,1,1)
        
    def on_button_clicked(self, id):
        for button in self.buttongroup.buttons():
            if button is self.buttongroup.button(id):
                print("%s was clicked!" % (button.text()))

                
app = QApplication(sys.argv)
screen = Window()
screen.show()
sys.exit(app.exec_())
