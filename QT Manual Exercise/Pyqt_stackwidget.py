from PyQt5.QtWidgets import *
import sys
class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        layout = QGridLayout()
        self.setLayout(layout)
        self.stackedwidget = QStackedWidget()
        layout.addWidget(self.stackedwidget, 0, 0)
        for x in range(1, 4):
            label = QLabel("Stack Child %i" % (x))
            self.stackedwidget.addWidget(label)
            button = QPushButton("Stack %i" % (x))
            button.page = x
            button.clicked.connect(self.on_button_clicked)
            layout.addWidget(button, x, 0)
    def on_button_clicked(self):
        button = self.sender()
        self.stackedwidget.setCurrentIndex(button.page - 1)
app = QApplication(sys.argv)
screen = Window()
screen.show()
sys.exit(app.exec_())