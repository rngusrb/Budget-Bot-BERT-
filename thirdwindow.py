import sys
from PyQt6.QtWidgets import *
from PyQt6 import uic
from PyQt6.QtCore import *
form_thirdwindow=uic.loadUiType("ui/thirdscreen.ui")[0]


class thirdwindow(QDialog,QWidget, form_thirdwindow):
    def __init__(self,date1):
        super(thirdwindow,self).__init__()
        self.initUI()
        self.showdata(date1)

    def initUI(self):
        self.setupUi(self)
        self.okay.clicked.connect(self.Home)
    def showdata(self,data2):
        use_sum=0
        earn_sum=0
        for i in range(len(data2)):
            usedata=data2[i]
            data=usedata.split(":")
            if data[3]=="expend":
                use_sum += int(data[2])
                self.use.append("{:<10}".format(str(data[1]))+": "+str(data[2]))

            elif data[3]=="earn":
                self.earn.append("{:<10}".format(str(data[1]))+": "+str(data[2]))
                earn_sum += int(data[2])
        self.result.setPlainText("총 이용금액: "+str(use_sum)+"\n"+"총 얻은금액: "+str(earn_sum)+"\n"+"총계: "+str(earn_sum-use_sum))



    def Home(self):
        self.close()