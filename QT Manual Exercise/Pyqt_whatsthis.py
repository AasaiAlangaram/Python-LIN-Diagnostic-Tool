from PyQt5.QtWidgets import *
import sys
class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        layout = QGridLayout()
        self.setLayout(layout)
        label = QLabel("Focus ComboBox and press SHIFT+F1")
        layout.addWidget(label)
        self.combobox = QComboBox()
        self.combobox.setWhatsThis("This is a 'WhatsThis' object description.")
        layout.addWidget(self.combobox)
app = QApplication(sys.argv)
screen = Window()
screen.show()
sys.exit(app.exec_())
