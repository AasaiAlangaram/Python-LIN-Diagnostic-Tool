from PyQt5.QtWidgets import *
import sys
class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        layout = QGridLayout()
        self.setLayout(layout)
        button = QPushButton("Launch")
        button.clicked.connect(self.on_button_clicked)
        layout.addWidget(button)
        self.wizard = QWizard()
    def on_button_clicked(self):
        self.wizard.open()
app = QApplication(sys.argv)
screen = Window()
screen.show()
sys.exit(app.exec_())