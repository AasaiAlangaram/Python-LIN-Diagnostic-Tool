from PyQt5.QtWidgets import *
import sys
class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        layout = QGridLayout()
        self.setLayout(layout)
        self.listwidget = QListWidget()
        self.listwidget.insertItem(0, "Orange")
        self.listwidget.insertItem(1, "Rose")
        self.listwidget.insertItem(2, "Brown")
        self.listwidget.insertItem(3, "Mauve")
        self.listwidget.insertItem(4, "Sapphire")
        self.listwidget.clicked.connect(self.listview_clicked)
        layout.addWidget(self.listwidget)
    def listview_clicked(self, qmodelindex):
        item = self.listwidget.currentItem()
        print(item.text())
app = QApplication(sys.argv)
screen = Window()
screen.show()
sys.exit(app.exec_())