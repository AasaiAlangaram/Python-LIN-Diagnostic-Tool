from PyQt5.QtWidgets import *
import sys



class Window(QWidget):
    def __init__(self):
       
        QWidget.__init__(self)
        self.radio()
    def radio(self):
        layout = QGridLayout()
        self.setLayout(layout)
        self.setWindowTitle("!!!Aasai Application!!!")
        self.setGeometry(200,200,500,300)
        self.setFixedSize(820,320)
        self.show()

        button = QPushButton("Exit")
        button.setToolTip("If you click this it will close this Window ")
        button.clicked.connect(self.exit_from_app)
        #button.setFlat(True)
        layout.addWidget(button, 11, 0)
        
        label=QLabel("1.Select your Nation:")
        layout.addWidget(label,0,0)
        
        radiobutton = QRadioButton("India")
        radiobutton.country = "Indian"
        radiobutton.toggled.connect(self.on_radio_button_toggled)
        layout.addWidget(radiobutton, 1, 0)
        
        radiobutton = QRadioButton("China")
        radiobutton.country = "Chinian"
        radiobutton.toggled.connect(self.on_radio_button_toggled)
        layout.addWidget(radiobutton, 2, 0)
        
        radiobutton = QRadioButton("Korea")
        radiobutton.country = "Korean"
        radiobutton.toggled.connect(self.on_radio_button_toggled)
        layout.addWidget(radiobutton, 3, 0)

        radiobutton = QRadioButton("Refugee")
        #radiobutton.setChecked(True)
        radiobutton.country = "Refugee"
        radiobutton.toggled.connect(self.on_radio_button_toggled)
        layout.addWidget(radiobutton, 4, 0)

        label=QLabel("2.Select your favourite programming language:")
        layout.addWidget(label,5,0)

        self.checkbox1 = QCheckBox("C")
        #self.checkbox1.setChecked(True)
        self.checkbox1.toggled.connect(self.checkbox_toggled)
        layout.addWidget(self.checkbox1, 6, 0)
        
        self.checkbox2 = QCheckBox("C++")
        self.checkbox2.toggled.connect(self.checkbox_toggled)
        layout.addWidget(self.checkbox2, 7, 0)

        self.checkbox3 = QCheckBox("Pyhton")
        self.checkbox3.toggled.connect(self.checkbox_toggled)
        layout.addWidget(self.checkbox3, 8, 0)
        
    def on_radio_button_toggled(self):
        
        radiobutton = self.sender()
        
        if radiobutton.isChecked():
            
            print("The Person is a %s" % (radiobutton.country))
            
    def checkbox_toggled(self):
        selected = []
        
        if self.checkbox1.isChecked():
            selected.append("C")
        if self.checkbox2.isChecked():
            selected.append("C++")
        if self.checkbox3.isChecked():
            selected.append("Python")
        print("He Likes: %s" % (" ".join(selected)))

    def exit_from_app(self):
        print("you clicked Exit Button\nIf you want to run again please press F5!@#")
        self.close()
        


app = QApplication(sys.argv)
screen = Window()
screen.show()
sys.exit(app.exec_())
