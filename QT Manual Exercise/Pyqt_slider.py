from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys
class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        layout = QGridLayout()
        self.setLayout(layout)
        
        slider = QSlider(Qt.Horizontal)
        
        slider.setMinimum(0)
        slider.setMaximum(5)
        slider.setTickInterval(1)
        slider.setTracking(True)
        slider.setTickPosition(QSlider.TicksBelow)
        layout.addWidget(slider, 0, 0)
        
        slider = QSlider(Qt.Vertical)

        slider.setValue(4)
        layout.addWidget(slider, 0, 1)
        
app = QApplication(sys.argv)
screen = Window()
screen.show()
sys.exit(app.exec_())
