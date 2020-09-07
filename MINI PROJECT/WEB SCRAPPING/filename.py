from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import resource_rc
from filename2 import Ui_otherWindow
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.widget = QtWidgets.QWidget(MainWindow)
        self.widget.setObjectName("widget")
        self.frame = QtWidgets.QFrame(self.widget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 801, 591))
        self.frame.setStyleSheet("*{\n"
"    background-image: url(:/newPrefix/img.jpg);\n"
"    color: rgb(255, 255, 255);\n"
"    font-size:15px;\n"
"    font-family:Century Gothic,sans-serif;\n"
"}\n"
"QFrame\n"
"{\n"
"border: solid 10px rgba(0,0,0);\n"
"    background-image: url(:/newPrefix/img.jpg);\n"
"\n"
"}\n"
"QLineEdit\n"
"{\n"
"border-style:outset;\n"
"border-radius:10px;\n"
"}\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(240, 300, 311, 91))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.button_clicked)
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(250, 220, 291, 61))
        self.lineEdit.setStyleSheet("color: rgb(255, 255, 255);")
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(250, 170, 291, 41))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.widget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    

    def button_clicked(self):
        url=self.lineEdit.text()
        self.check(url)
    def check(self,url):
        website=url
        import validators
        valid=validators.url(website)
        if valid==True:
            self.scrapeurl(url)
            self.openwindow()
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("please enter a valid url")
            msg.exec_() 
    def scrapeurl(self,url):
        website=url
        from urllib.request import Request, urlopen
        from bs4 import BeautifulSoup
        req = Request(website , headers={'User-Agent': 'Mozilla/5.0'})
        page = urlopen(req)
        html = page.read().decode("utf-8")
        soup = BeautifulSoup(html,"html.parser")
        for script in soup(["script", "style","head","title","meta","[document]"]):
            script.decompose()
        strips = list(soup.stripped_strings)
        makeitastring = ''.join(map(str, strips))
        with open('browsers.txt', 'w',encoding="utf-8") as f:
            f.writelines(makeitastring)
    def openwindow(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_otherWindow()
        self.ui.setupUi(self.window)
        self.window.show()
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "SUBMIT"))
        self.label.setText(_translate("MainWindow", "                       Enter Url"))

        
def main():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
main()