from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")

        self.board = QtWidgets.QTextEdit(Form)
        self.board.setObjectName("board")
        self.verticalLayout.addWidget(self.board)
        self.text = QtWidgets.QPushButton(Form)
        self.text.setObjectName("text")
        self.verticalLayout.addWidget(self.text)
        self.text.clicked.connect(self.add)

        self.tab = QtWidgets.QPushButton(Form)
        self.tab.setObjectName("tab")
        self.verticalLayout.addWidget(self.tab)
        self.tab.clicked.connect(self.tab_)

        self.deb = QtWidgets.QPushButton(Form)
        self.deb.setObjectName("debug")
        self.verticalLayout.addWidget(self.deb)
        self.deb.clicked.connect(self.print_out)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.text.setText(_translate("Form", "Add text"))
        self.tab.setText(_translate("Form", "Add tab"))
        self.deb.setText("debug")
    def add(self):
        print("Add text success")
        self.board.insertHtml("<p><span style='background-color:yellow;'>A. confidence</span></p><pre>  </pre>")
        # self.board.moveCursor(QtGui.QTextCursor.EndOfLine)
    def tab_(self):
        print("Add tab success!")
        self.board.insertHtml("<pre>        </pre>")
        # self.board.insertHtml("\t")
    def print_out(self):
        print(self.board.toHtml())

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
