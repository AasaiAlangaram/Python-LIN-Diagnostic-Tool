from PyQt5.QtWidgets import *
import sys
class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        layout = QGridLayout()
        self.setLayout(layout)
        dockwidget = QDockWidget()
        dockwidget.setFeatures(QDockWidget.DockWidgetClosable | QDockWidget.DockWidgetVerticalTitleBar)
        layout.addWidget(dockwidget)
        treewidget = QTreeWidget()
        dockwidget.setWidget(treewidget)
        label = QLabel("DockWidget is docked")
        layout.addWidget(label)
app = QApplication(sys.argv)
screen = Window()
screen.show()
sys.exit(app.exec_())