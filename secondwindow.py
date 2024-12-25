from PyQt6.QtWidgets import *
from PyQt6 import uic
import amoney
import datetime
form_secondwindow=uic.loadUiType("ui/secondwindow.ui")[0]
now=datetime.datetime.now()

class secondwindow(QDialog,QWidget, form_secondwindow):
    def __init__(self,date1,date2):
        super(secondwindow,self).__init__()
        self.initUI()
        self.show()
        self.dateM=date1
        self.dateD=date2
        self.val1=0
        self.checknum=0
        print(date1,date2)

    def initUI(self):
        self.setupUi(self)
        self.okay.clicked.connect(self.inputdata)
        self.okay.clicked.connect(self.Home)
        self.expend.clicked.connect(self.func)
        self.okay.clicked.connect(self.check)
        self.earn.clicked.connect(self.func2)
    def func(self):
        self.val1=1

    def func2(self):
        self.val1=2
    def check(self):
        if self.dateM==now.month:
            if self.expend.clicked:
                if self.checknum not in [1,2,3,4]:
                    self.ui = amoney.amoney()
                    self.ui.close()
                    self.checknum = self.ui.mfunc3()



    def inputdata(self):
        try:
            if self.amount.text() != str(0):
                bb=int(self.amount.text())

                try:
                    with open("save/data" + str(self.dateM) + ".txt", "a",encoding='utf-8') as file:
                        if self.val1==1:
                            file.write(str(self.dateD) + ":")
                            file.write(self.usingname.text() + ":")
                            file.write(self.amount.text()+ ":")
                            file.write("expend"+ ":")
                            file.write(self.ca.currentText()+"\n")
                            file.close()
                        elif self.val1 == 2:
                            file.write(str(self.dateD) + ":")
                            file.write(self.usingname.text() + ":")
                            file.write(self.amount.text() + ":")
                            file.write("earn" + ":")
                            file.write(self.ca.currentText()+"\n")
                            file.close()


                except FileNotFoundError as e1:
                    with open("save/data" + str(self.dateM) + ".txt", "a",encoding='utf-8') as file:
                        if self.val1 == 1:
                            file.write(str(self.dateD) + ":")
                            file.write(self.usingname.text() + ":")
                            file.write(self.amount.text() + ":")
                            file.write("expend" + ":")
                            file.write(self.ca.currentText()+"\n")
                            file.close()
                        elif self.val1==2:
                            file.write(str(self.dateD) + ":")
                            file.write(self.usingname.text() + ":")
                            file.write(self.amount.text() + ":")
                            file.write("earn" + ":")
                            file.write(self.ca.currentText()+"\n")
                            file.close()

            else:
                print("0원은 입력이 불가합니다")
                self.Home()

        except ValueError:
            print("숫자를 입력하세요")
            self.Home()


    def Home(self):
        self.close()
