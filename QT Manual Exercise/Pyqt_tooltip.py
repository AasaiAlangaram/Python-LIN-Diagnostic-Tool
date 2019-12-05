from PyQt5.QtWidgets import *
import sys
class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        layout = QGridLayout()
        self.setLayout(layout)
        button = QPushButton("Simple ToolTip")
        button.setToolTip("This ToolTip simply displays text.")
        layout.addWidget(button, 0, 0)
        button = QPushButton("Formatted ToolTip")
        button.setToolTip("<b>Formatted text</b> can also be displayed.")
        layout.addWidget(button, 1, 0)
app = QApplication(sys.argv)
screen = Window()
screen.show()
sys.exit(app.exec_())
