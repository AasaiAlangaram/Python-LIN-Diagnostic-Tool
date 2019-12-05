from PyQt5.QtWidgets import *
import sys
#this line enable script to receive command from python command line
class Window(QWidget):#QWidget is the base class of all user interface object

    def __init__(self):
        QWidget.__init__(self)
        #initialize QWidget
        self.setWindowTitle("Hello")
        #setwindowTitle is the method of Baseclass
        layout = QGridLayout()
        self.setLayout(layout)
        label = QLabel("Hello, World!")
        #passing "hello world" in Qlabel method
        layout.addWidget(label, 0, 0)
        #passing parameters in addwidget method
#app = QApplication(sys.argv)  #We are creating a QApplication object, and saving it to "app"
#Here, we pass this sys.argv argument because sys.argv allows us to pass command line arguments to the application.
#The idea of sys.argv is to allow you to pass arguments through to Python from the command line.
#sys.argv accepts arguments from python command line
#screen = Window()
#assign Window class to object screen
#screen.show()
#sys.exit(app.exec_())
