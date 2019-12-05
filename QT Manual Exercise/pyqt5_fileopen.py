from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_TestQFileDialog(object):
    def _open_file_dialog(self):
        directory = str(QtWidgets.QFileDialog.getExistingDirectory())
        self.lineEdit.setText('{}'.format(directory))

    def _set_text(self, text):
        return text

    def setupUi(self, TestQFileDialog):
        TestQFileDialog.setObjectName("TestQFileDialog")
        TestQFileDialog.resize(240, 320)

        self.toolButtonOpenDialog = QtWidgets.QToolButton(TestQFileDialog)
        self.toolButtonOpenDialog.setGeometry(QtCore.QRect(210, 10, 25, 19))
        self.toolButtonOpenDialog.setObjectName("toolButtonOpenDialog")
        self.toolButtonOpenDialog.clicked.connect(self._open_file_dialog)

        self.lineEdit = QtWidgets.QLineEdit(TestQFileDialog)
        self.lineEdit.setEnabled(False)
        self.lineEdit.setGeometry(QtCore.QRect(10, 10, 191, 20))
        self.lineEdit.setObjectName("lineEdit")

        self.retranslateUi(TestQFileDialog)
        QtCore.QMetaObject.connectSlotsByName(TestQFileDialog)

    def retranslateUi(self, TestQFileDialog):
        _translate = QtCore.QCoreApplication.translate
        TestQFileDialog.setWindowTitle(_translate("TestQFileDialog", "Dialog"))
        self.toolButtonOpenDialog.setText(_translate("TestQFileDialog", "..."))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TestQFileDialog = QtWidgets.QDialog()
    ui = Ui_TestQFileDialog()
    ui.setupUi(TestQFileDialog)
    TestQFileDialog.show()
    sys.exit(app.exec_())