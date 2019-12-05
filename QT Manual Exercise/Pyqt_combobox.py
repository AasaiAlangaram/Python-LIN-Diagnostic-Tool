from PyQt5.QtWidgets import *
import sys
class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        layout = QGridLayout()
        self.setLayout(layout)
        self.combobox = QComboBox()
        self.combobox.addItem("Birch")
        self.combobox.addItem("Oak")
        self.combobox.addItem("Sycamore")
        self.combobox.currentTextChanged.connect(self.combobox_changed)
        layout.addWidget(self.combobox)
    def combobox_changed(self):
        text = self.combobox.currentText()
        print(text)
app = QApplication(sys.argv)
screen = Window()
screen.show()
sys.exit(app.exec_())