from PyQt5.QtWidgets import *
import sys
class Dialog(QWidget):
    def __init__(self):
                QWidget.__init__(self)
                layout = QGridLayout()
                self.setLayout(layout)
                fontcombobox = QFontComboBox()
                fontcombobox.currentFontChanged.connect(self.on_font_changed)
                layout.addWidget(fontcombobox)
    def on_font_changed(self):
        fontcombobox = self.sender()
        font = fontcombobox.currentFont()
        print("Selected font: %s" % (font.family()))
app = QApplication(sys.argv)
screen = Dialog()
screen.show()
sys.exit(app.exec_())