from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
class Ui_otherWindow(object):
    def setupUi(self, otherWindow):
        otherWindow.setObjectName("otherWindow")
        otherWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(otherWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, -10, 801, 611))
        self.frame.setStyleSheet("*{\n"
"    color: rgb(255, 255, 255);\n"
"    font-size:15px;\n"
"    font-family:Century Gothic,sans-serif;\n"
"}\n"
"QFrame\n"
"{\n"
"border: solid 10px rgba(0,0,0);\n"
"background-image: url(:/newPrefix/img.jpg);\n"
"\n"
"}\n"
"QLabel\n"
"{\n"
"background:#eeeeee;\n"
"border-style:outset;\n"
"border-radius:10px;\n"
"}\n"
"QPushButton\n"
"{\n"
"background: rgb(0, 0, 0);\n"
"border-style:outset;\n"
"border-radius:10px;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(190, 140, 451, 41))
        self.label.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(270, 260, 241, 81))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.button_clicked)
        otherWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(otherWindow)
        self.statusbar.setObjectName("statusbar")
        otherWindow.setStatusBar(self.statusbar)

        self.retranslateUi(otherWindow)
        QtCore.QMetaObject.connectSlotsByName(otherWindow)
    
    def button_clicked(self):
        f = open("browsers.txt", "r",encoding='utf-8')
        text=f.read()
        self.encryption(text)
        
    def encryption(self,text):
        data=text
        modal=['can', 'could', 'may', 'might', 'will', 'would', 'shall', 'should', 'must']
        article=['a','an','the']
        preposition=['about','above','across','after','against','among','around','at','before','behind','below',
                     'beside','between','by','down','during','for''from''in''inside''into''near''of''off''on''out''over''through''to''toward''under''up''with']
        conjuction=['and', 'but', 'for', 'nor', 'or', 'so','yet' ]
        check_val=data.split(' ')
        string_list = [each_string.lower() for each_string in check_val]
        nmodal=0
        narticle=0
        npreposition=0
        nconjuction=0
        for i in string_list:
            if i in modal:
                nmodal+=1
            elif i in article:
                narticle+=1
            elif i in preposition:
                npreposition+=1
            elif i in conjuction:
                nconjuction+=1
        add=nmodal+narticle+npreposition+nconjuction
        self.rsa(add)
    def rsa(self,add):
        import random
        number=add
        from decimal import Decimal 
        def gcd(a,b): 
            if b==0: 
                return a 
            else: 
                return gcd(b,a%b)
        fo = open('primes-to-100k.txt', 'r')
        lines = fo.read().splitlines()
        fo.close()
        rand1 = random.randint(100, 300)
        rand2 = random.randint(100, 300)
        p = int(lines[rand1])
        q = int(lines[rand2])
        n = p*q 
        t = (p-1)*(q-1) 
  
        for e in range(2,t): 
            if gcd(e,t)== 1: 
                    break
        for i in range(1,10): 
            x = 1 + i*t 
            if x % e == 0: 
                d = int(x/e) 
                break
        ctt = Decimal(0) 
        ctt =pow(number,e) 
        ct = ctt % n 
  
        dtt = Decimal(0) 
        dtt = pow(ct,d) 
        dt = dtt % n 
        msg = QMessageBox()
        msg.setWindowTitle("Encrypyted key")
        msg.setText('n = '+str(n)+' e = '+str(e)+' t = '+str(t)+' d = '+str(d)+' cipher text = '+str(ct)+' decrypted text = '+str(dt))
        msg.exec_()
       
        
    def retranslateUi(self, otherWindow):
        _translate = QtCore.QCoreApplication.translate
        otherWindow.setWindowTitle(_translate("otherWindow", "MainWindow"))
        self.label.setText(_translate("otherWindow", "PRESS BUTTON TO GENERATE ENCRYPTED URL"))
        self.pushButton.setText(_translate("otherWindow", "PushButton"))

import resource_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    otherWindow = QtWidgets.QMainWindow()
    ui = Ui_otherWindow()
    ui.setupUi(otherWindow)
    otherWindow.show()
    sys.exit(app.exec_())

