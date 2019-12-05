from PyQt5.QtWidgets import *
import sys
class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        layout = QGridLayout()
        self.setLayout(layout)
        self.checkbox1 = QCheckBox("Kestrel")
        self.checkbox1.setChecked(True)
        self.checkbox1.toggled.connect(self.checkbox_toggled)
        layout.addWidget(self.checkbox1, 0, 0)
        self.checkbox2 = QCheckBox("Sparrowhawk")
        self.checkbox2.toggled.connect(self.checkbox_toggled)
        layout.addWidget(self.checkbox2, 1, 0)
        self.checkbox3 = QCheckBox("Hobby")
        self.checkbox3.toggled.connect(self.checkbox_toggled)
        layout.addWidget(self.checkbox3, 2, 0)
    def checkbox_toggled(self):
        selected = []
        if self.checkbox1.isChecked():
            selected.append("Kestrel")
        if self.checkbox2.isChecked():
            selected.append("Sparrowhawk")
        if self.checkbox3.isChecked():
            selected.append("Hobby")
        print("Selected: %s" % (" ".join(selected)))
app = QApplication(sys.argv)
screen = Window()
screen.show()
sys.exit(app.exec_())
