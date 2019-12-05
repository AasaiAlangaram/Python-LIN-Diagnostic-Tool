from PyQt5.QtWidgets import *
import sys

class Window(QWidget):
    
    def __init__(self):
        
        QWidget.__init__(self)
        layout = QGridLayout()
        self.setLayout(layout)

        self.setWindowTitle("!!!Aasai Application!!!")
        self.setGeometry(200,200,500,300)
        self.setFixedSize(820,320)
        self.show()

        self.button = QPushButton("your name:")
        #self.button.clicked.connect(self.on_button_clicked)
        layout.addWidget(self.button,0,0)

        self.button = QPushButton("country name:")
        layout.addWidget(self.button,1,0)

        self.button = QPushButton("Father name:")
        layout.addWidget(self.button,2,0)

        self.button1 = QPushButton("Print in PY-Shell")
        self.button1.clicked.connect(self.return_pressed)
        self.button1.move(100,100)
        #self.button1.setSizePolicy(QtGui.QSizePolicy.Preferred,QtGui.QSizePolicy.Expanding)
        layout.addWidget(self.button1,4,1)

        self.button2 = QPushButton("Close")
        self.button2.clicked.connect(self.on_button_clicked)
        layout.addWidget(self.button2,5,1)
        
    
        self.lineedit1 = QLineEdit()
        self.lineedit1.returnPressed.connect(self.return_pressed)
        layout.addWidget(self.lineedit1,0,1)

        self.lineedit2 = QLineEdit()
        self.lineedit2.returnPressed.connect(self.return_pressed)
        layout.addWidget(self.lineedit2,1,1)

        self.lineedit3 = QLineEdit()
        self.lineedit3.returnPressed.connect(self.return_pressed)
        layout.addWidget(self.lineedit3,2,1)

    def on_button_clicked(self):
     

        
            #print("The button was pressed!")
            self.close()
        
        
    def return_pressed(self):
        
            print("His name is:", self.lineedit1.text())
            print("He is from :", self.lineedit2.text())
            print("His father name is:", self.lineedit3.text())
        
app = QApplication(sys.argv)
screen = Window()
screen.show()
sys.exit(app.exec_())

