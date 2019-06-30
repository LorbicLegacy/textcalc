# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'textcalc_ui.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import webbrowser

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):

        ####  Variables  ####

        self.chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'


        self.style_sheet = """
        QWidget{
            background-color : lightgray;
        }

        QFrame#frame{
            
        }
        QPushButton#pushButton,QPushButton#pushButton_2{
            border : 1px solid wheat;
            border-radius : 15%;

        }
        QPushButton#pushButton{
            background-color : gray;
            color : white;
        }
        QPushButton#pushButton:hover{
            background-color : black;
        }

        QPushButton#pushButton_2{
            background-color : skyblue;
            color : white;
        }
        QPushButton#pushButton_2:hover{
            background-color : #0082fc;
        }

        QPushButton#calculate_btn{
            border : 1px solid lightgray;
            border-radius : 45%;
            background : qlineargradient(x1:0 y1:1, x2:1 y2:0, stop:0 blue, stop:1 violet);
        }
        QPushButton#calculate_btn:hover{
            border : 1px solid yellow;
            border-radius : 45%;
            background : qlineargradient(x1:1 y1:1, x2:0 y2:0, stop:0 blue, stop:1 #fea201);
            color : qlineargradient(x1:1 y1:1, x2:0 y2:1, stop:0 yellow, stop:1 pink);
        }

        QLabel#label_10:hover{
        color : red;
        }

        QLabel#nameOfApp:hover{
            background : qlineargradient(x1:1 y1:1, x2:0 y2:1, stop:0 yellow, stop:1 #d83ed6);
            
        }



        """


        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 485)
        MainWindow.setMinimumSize(QtCore.QSize(800, 485))
        MainWindow.setMaximumSize(QtCore.QSize(800, 485))
        font = QtGui.QFont()
        font.setPointSize(5)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.nameOfApp = QtWidgets.QLabel(self.centralwidget)
        self.nameOfApp.setGeometry(QtCore.QRect(300, 10, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Blackout")
        font.setPointSize(36)
        self.nameOfApp.setFont(font)
        self.nameOfApp.setAlignment(QtCore.Qt.AlignCenter)
        self.nameOfApp.setObjectName("nameOfApp")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(290, 50, 211, 21))
        font = QtGui.QFont()
        font.setFamily("Costura Rg")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.textInBox = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.textInBox.setGeometry(QtCore.QRect(20, 90, 581, 91))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textInBox.setFont(font)
        self.textInBox.setReadOnly(False)
        self.textInBox.setPlainText("")
        self.textInBox.setObjectName("textInBox")
        self.calculate_btn = QtWidgets.QPushButton(self.centralwidget)
        self.calculate_btn.setGeometry(QtCore.QRect(630, 90, 151, 91))
        font = QtGui.QFont()
        font.setFamily("Lobster Two")
        font.setPointSize(23)
        font.setBold(True)
        font.setWeight(75)
        self.calculate_btn.setFont(font)
        self.calculate_btn.setObjectName("calculate_btn")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(50, 190, 701, 191))
        font = QtGui.QFont()
        font.setFamily("NewRocker")
        font.setPointSize(16)
        self.frame.setFont(font)
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setObjectName("frame")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(50, 30, 111, 41))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(180, 30, 111, 41))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(310, 30, 111, 41))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(540, 30, 111, 41))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(430, 30, 111, 41))
        self.label_7.setObjectName("label_7")
        self.nums_bx = QtWidgets.QLabel(self.frame)
        self.nums_bx.setGeometry(QtCore.QRect(50, 90, 81, 41))
        font = QtGui.QFont()
        font.setFamily("OCR A Std")
        font.setBold(True)
        font.setWeight(75)
        self.nums_bx.setFont(font)
        self.nums_bx.setFrameShape(QtWidgets.QFrame.Box)
        self.nums_bx.setText("")
        self.nums_bx.setAlignment(QtCore.Qt.AlignCenter)
        self.nums_bx.setObjectName("nums_bx")
        self.caps_bx = QtWidgets.QLabel(self.frame)
        self.caps_bx.setGeometry(QtCore.QRect(180, 90, 81, 41))
        font = QtGui.QFont()
        font.setFamily("OCR A Std")
        font.setBold(True)
        font.setWeight(75)
        self.caps_bx.setFont(font)
        self.caps_bx.setFrameShape(QtWidgets.QFrame.Box)
        self.caps_bx.setText("")
        self.caps_bx.setAlignment(QtCore.Qt.AlignCenter)
        self.caps_bx.setObjectName("caps_bx")
        self.smls_bx = QtWidgets.QLabel(self.frame)
        self.smls_bx.setGeometry(QtCore.QRect(300, 90, 81, 41))
        font = QtGui.QFont()
        font.setFamily("OCR A Std")
        font.setBold(True)
        font.setWeight(75)
        self.smls_bx.setFont(font)
        self.smls_bx.setFrameShape(QtWidgets.QFrame.Box)
        self.smls_bx.setText("")
        self.smls_bx.setAlignment(QtCore.Qt.AlignCenter)
        self.smls_bx.setObjectName("smls_bx")
        self.space_bx = QtWidgets.QLabel(self.frame)
        self.space_bx.setGeometry(QtCore.QRect(420, 90, 81, 41))
        font = QtGui.QFont()
        font.setFamily("OCR A Std")
        font.setBold(True)
        font.setWeight(75)
        self.space_bx.setFont(font)
        self.space_bx.setFrameShape(QtWidgets.QFrame.Box)
        self.space_bx.setText("")
        self.space_bx.setAlignment(QtCore.Qt.AlignCenter)
        self.space_bx.setObjectName("space_bx")
        self.symbol_bx = QtWidgets.QLabel(self.frame)
        self.symbol_bx.setGeometry(QtCore.QRect(540, 90, 81, 41))
        font = QtGui.QFont()
        font.setFamily("OCR A Std")
        font.setBold(True)
        font.setWeight(75)
        self.symbol_bx.setFont(font)
        self.symbol_bx.setFrameShape(QtWidgets.QFrame.Box)
        self.symbol_bx.setText("")
        self.symbol_bx.setAlignment(QtCore.Qt.AlignCenter)
        self.symbol_bx.setObjectName("symbol_bx")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(50, 400, 701, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.frame_2.setFont(font)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.pushButton = QtWidgets.QPushButton(self.frame_2)
        self.pushButton.setGeometry(QtCore.QRect(600, 10, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        self.pushButton.setFont(font)
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 10, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_8 = QtWidgets.QLabel(self.frame_2)
        self.label_8.setGeometry(QtCore.QRect(220, 10, 131, 31))
        self.label_8.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.frame_2)
        self.label_9.setGeometry(QtCore.QRect(380, 10, 101, 31))
        self.label_9.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.frame_2)
        self.label_10.setGeometry(QtCore.QRect(340, 10, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label_10.setFont(font) #heart
        self.label_10.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 16))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        MainWindow.setStyleSheet(self.style_sheet)


        #### main functional coding starts here

        self.calculate_btn.clicked.connect(self.calculate)
        self.pushButton.clicked.connect(self.open_github)
        self.pushButton_2.clicked.connect(self.open_twitter)



        #########################################
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "TEXTCALC"))
        MainWindow.setWindowIcon(QtGui.QIcon("icon.png"))

        self.nameOfApp.setText(_translate("MainWindow", "TEXTCALC"))
        self.label.setText(_translate("MainWindow", "character calculator"))
        self.textInBox.setPlaceholderText(_translate("MainWindow", "Enter text here then press calculate"))
        self.calculate_btn.setText(_translate("MainWindow", "Calculate"))
        self.label_3.setText(_translate("MainWindow", "Numbers "))
        self.label_4.setText(_translate("MainWindow", "Capitals"))
        self.label_5.setText(_translate("MainWindow", "Smalls"))
        self.label_6.setText(_translate("MainWindow", "Symbols"))
        self.label_7.setText(_translate("MainWindow", "Space"))
        self.label_8.setText(_translate("MainWindow", "Developed With"))
        self.label_9.setText(_translate("MainWindow", "By Vikas Patel"))
        self.label_10.setText(_translate("MainWindow", "♥"))
        self.pushButton.setText(_translate("MainWindow", "GitHub"))
        self.pushButton_2.setText(_translate("MainWindow", "Twitter"))


    ### user functions 
    def get_text(self):
        self.text = self.textInBox.toPlainText()
        return (self.text)

    def calculate(self):

        data = self.get_text()
        alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        caps = list(alpha)
        smls = list(alpha.lower())
        nums = list("0123456789")

        self.list_of_chars = list(data)
        self.nos = 0
        self.capitals = 0
        self.smalls = 0
        self.spaces = 0
        self.special_symbols = 0
        
        for char in self.list_of_chars :
            if " " in char:
                self.spaces += 1
            elif char in caps :
                self.capitals += 1
            elif char in smls :
                self.smalls += 1
            elif char in nums:
                self.nos += 1
            else :
                self.special_symbols += 1
        self.place_result()



    def place_result(self):

        self.nums_bx.setText(str(self.nos))
        self.caps_bx.setText(str(self.capitals))
        self.smls_bx.setText(str(self.smalls))
        self.space_bx.setText(str(self.spaces))
        self.symbol_bx.setText(str(self.special_symbols))


    def open_github(self):
        webbrowser.get(self.chrome_path).open("vikaspatelp83.github.io")

    def open_twitter(self):
        webbrowser.get(self.chrome_path).open("twitter.com/devdp430")
        


####################################################################################

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
