from PyQt5.QtWidgets import *
import sys
class FontDialog(QFontDialog):
    def __init__(self):
        QFontDialog.__init__(self)
        self.fontSelected.connect(self.on_font_selected)
    def on_font_selected(self):
        font = self.currentFont()
        print("Name: %s" % (font.family()))
        print("Size: %i" % (font.pointSize()))
        print("Italic: %s" % (font.italic()))
        print("Underline: %s" % (font.underline()))
        print("Strikeout: %s" % (font.strikeOut()))
    def run(self):
        self.show()
app = QApplication(sys.argv)
screen = FontDialog()
screen.run()
sys.exit(app.exec_())