from PyQt5 import QtCore, QtGui, QtWidgets
from help import HelpWindow
from process import Analyze
import threading, time, os

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.helpWindow = HelpWindow()
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(714, 588)
        MainWindow.setAnimated(True)
        try:
            with open(resource_path("Ubuntu.qss"), "r") as f:
                theme = f.read()
                MainWindow.setStyleSheet(theme)
        except:
            pass
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("font: 8pt \"Leelawadee UI\";\n"
"font-size: 14px")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.ButtonTab = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ButtonTab.sizePolicy().hasHeightForWidth())
        self.ButtonTab.setSizePolicy(sizePolicy)
        self.ButtonTab.setMinimumSize(QtCore.QSize(150, 0))
        self.ButtonTab.setMaximumSize(QtCore.QSize(350, 16777215))
        self.ButtonTab.setObjectName("ButtonTab")
        self.Button = QtWidgets.QVBoxLayout(self.ButtonTab)
        self.Button.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.Button.setObjectName("Button")
        self.label = QtWidgets.QLabel(self.ButtonTab)
        self.label.setStyleSheet("")
        self.label.setObjectName("label")
        self.Button.addWidget(self.label)
        self.bar = QtWidgets.QProgressBar(self.ButtonTab)
#         self.bar.setStyleSheet("QProgressBar {\n"
# "    text-align:center;\n"
# "}")
        self.bar.setProperty("value", 0)
        self.bar.setTextVisible(True)
        self.bar.setOrientation(QtCore.Qt.Horizontal)
        self.bar.setInvertedAppearance(False)
        self.bar.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.bar.setObjectName("bar")
        self.bar.setFormat("")
        self.Button.addWidget(self.bar)
        self.label_3 = QtWidgets.QLabel(self.ButtonTab)
        self.label_3.setObjectName("label_3")
        #Button Tab
        self.Button.addWidget(self.label_3)
        self.preAnswer = QtWidgets.QTextEdit(self.ButtonTab)
        self.preAnswer.setReadOnly(True)
        self.preAnswer.setObjectName("preAnswer")
        self.Button.addWidget(self.preAnswer)
        self.notice = QtWidgets.QLabel(self.ButtonTab)
        self.Button.addWidget(self.notice)

        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.Button.addItem(spacerItem)
        self.exam = QtWidgets.QPushButton(self.ButtonTab)
        self.exam.setStyleSheet("")
        self.exam.setObjectName("exam")
        self.Button.addWidget(self.exam)
        self.answer = QtWidgets.QPushButton(self.ButtonTab)
        self.answer.setObjectName("answer")
        self.Button.addWidget(self.answer)

        self.actionLayout = QtWidgets.QHBoxLayout()
        self.actionLayout.setObjectName("actionLayout")

        self.progress = QtWidgets.QPushButton(self.ButtonTab)
        self.progress.setObjectName("progress")
        self.actionLayout.addWidget(self.progress)

        self.save = QtWidgets.QPushButton(self.ButtonTab)
        self.save.setObjectName("save")
        self.actionLayout.addWidget(self.save)
        self.Button.addLayout(self.actionLayout)


        self.gridLayout.addWidget(self.ButtonTab, 1, 0, 1, 1)

        #Tab xem trước
        self.PreviewTab = QtWidgets.QFrame(self.centralwidget)
        self.PreviewTab.setMinimumSize(QtCore.QSize(300, 0))
        self.PreviewTab.setObjectName("PreviewTab")
        self.Preview = QtWidgets.QVBoxLayout(self.PreviewTab)
        self.Preview.setObjectName("Preview")
        self.label_2 = QtWidgets.QLabel(self.PreviewTab)
        self.label_2.setObjectName("label_2")
        self.Preview.addWidget(self.label_2)
        self.preExam = QtWidgets.QTextEdit(self.PreviewTab)
        self.preExam.setReadOnly(True)
        self.preExam.setObjectName("preExam")
        self.Preview.addWidget(self.preExam)
        self.gridLayout.addWidget(self.PreviewTab, 1, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        #Thanh menu
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 476, 21))
        self.menubar.setObjectName("menubar")
        self.menuMade_by_thiendev_with_3 = QtWidgets.QMenu(self.menubar)
        self.menuMade_by_thiendev_with_3.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Vinhan")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.menuMade_by_thiendev_with_3.setFont(font)
        self.menuMade_by_thiendev_with_3.setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.menuMade_by_thiendev_with_3.setMouseTracking(True)
        self.menuMade_by_thiendev_with_3.setStyleSheet("font: 75 8pt \"Vinhan\";")
        self.menuMade_by_thiendev_with_3.setTearOffEnabled(True)
        self.menuMade_by_thiendev_with_3.setObjectName("menuMade_by_thiendev_with_3")
        self.menuHDSD = QtWidgets.QMenu(self.menubar)
        self.menuHDSD.setObjectName("menuHDSD")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        self.stt = QtWidgets.QLabel(MainWindow)
        self.stt.setObjectName("stt")
        self.verticalLayout.addWidget(self.stt)
        MainWindow.setStatusBar(self.statusbar)
        self.actionHelp = QtWidgets.QAction(MainWindow)
        self.actionHelp.setObjectName("actionHelp")
        self.actionHelp.triggered.connect(self.helpWindow.reshow)
        #rect["x"] + rect["w"], rect["y"] + rect["h"]
        self.menuHDSD.addAction(self.actionHelp)
        self.menubar.addAction(self.menuMade_by_thiendev_with_3.menuAction())
        self.menubar.addAction(self.menuHDSD.menuAction())
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.setupFunc()
        # Biến dữ liệu
        self.examPath = None
        self.answerPath = None
        self.savePath = None
        self.doc = Analyze()
    # Thiết lập kết nối, tín hiệu
    def setupFunc(self):
        self.exam.clicked.connect(self.examFunc)
        self.answer.clicked.connect(self.answerFunc)
        self.progress.clicked.connect(self.working)
        self.save.clicked.connect(self.save_to)
    def updateStt(self, text):
        self.stt.setText(text)
    def progressUpdate(self):
        for i in range(100):
            time.sleep(0.01)
            self.bar.setProperty("value", i + 1)
        time.sleep(2)
        self.bar.setProperty("value", 0)

    def examFunc(self):
        self.examPath = self.openFile("Chọn đề:")
        if self.examPath:
            self.doc.getExam(self.examPath)
            self.preExam.clear()
            [self.preExam.append(i) for i in self.doc.data].clear()
    def answerFunc(self):
        self.answerPath = self.openFile("Chọn đáp án:")
        if self.answerPath:
            self.doc.getAnswer(self.answerPath)
            self.preAnswer.clear()
            [self.preAnswer.append(f"{i + 1}. {a}") for i, a in enumerate(self.doc.answer)].clear()
    def working(self):
        self.updateStt("Trạng thái: Đang thực hiện!")
        self.doc.makeDocument()
        thread = threading.Thread(target=self.progressUpdate)
        thread.start()
        time.sleep(1.5)
        self.preExam.clear()
        self.preExam.setHtml("".join(["".join(i) if type(i) == list else i for i in self.doc.preview_dat]))
    def save_to(self):
        if self.doc.is_process_complete:
            self.savePath = self.saveFile()
            if self.savePath:
                self.doc.saveDocument(self.savePath)
                self.updateStt("Trạng thái: Xong, đã lưu vào ~ " + self.savePath + " ~")

    def openFile(self, cap):
        return QtWidgets.QFileDialog.getOpenFileName(caption=cap, filter="Tài liệu (*.docx)")[0]
    def saveFile(self):
        return QtWidgets.QFileDialog.getSaveFileName(caption="Lưu đề:", filter="Tài liệu (*.docx)")[0]
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Auto Answer for Word"))
        self.label.setText(_translate("MainWindow", "Tiến độ:"))
        self.label_3.setText(_translate("MainWindow", "Đáp án:"))
        self.notice.setText(_translate("MainWindow", " ** Lưu ý chọn đúng loại file!"))
        self.preAnswer.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Leelawadee UI\'; font-size:14px; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Segoe UI Semibold\'; font-weight:56;\"><br /></p></body></html>"))
        self.exam.setText(_translate("MainWindow", "Chọn đề"))
        self.answer.setText(_translate("MainWindow", "Chọn đáp án"))
        self.progress.setText(_translate("MainWindow", "Tiến hành"))
        self.save.setText(_translate("MainWindow", "Lưu!"))
        self.label_2.setText(_translate("MainWindow", "Xem trước:"))
        self.stt.setText(_translate("MainWindow", "Trạng thái: "))
        self.preExam.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Leelawadee UI\'; font-size:14px; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Segoe UI Semibold\'; font-weight:56;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Segoe UI Semibold\'; font-weight:56;\"><br /></p></body></html>"))
        self.menuMade_by_thiendev_with_3.setToolTip(_translate("MainWindow", "<3"))
        self.menuMade_by_thiendev_with_3.setTitle(_translate("MainWindow", "Made by thiendev with <3"))
        self.menuHDSD.setTitle(_translate("MainWindow", "Dùng như nào?"))
        self.actionHelp.setText(_translate("MainWindow", "Cách dùng <.>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()

    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
