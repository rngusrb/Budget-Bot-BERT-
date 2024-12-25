import calendar
from datetime import datetime
from PyQt6.QtWidgets import *
from PyQt6 import uic
now=datetime.now()
form_amwindow=uic.loadUiType("ui/am.ui")[0]
class amoney(QDialog, QWidget, form_amwindow):
    def __init__(self):
        super(amoney,self).__init__()
        self.initUI()
        self.show()
        self.val1 = 0
        self.msg = QMessageBox()
        self.num=0
    def initUI(self):
        self.setupUi(self)
        self.okay.clicked.connect(self.Home)
        self.check.clicked.connect(self.inputdata)
        self.check.clicked.connect(self.func2)
        self.pushButton.clicked.connect(self.clear)
        self.check.clicked.connect(self.dshow)
        self.pushButton.clicked.connect(self.dshow)
        self.func2()
        self.dshow()

    def dshow(self):
        aa=0
        sum=0
        try:
            with open("save/data" + str(now.month)+".txt", "r",encoding='utf-8') as file:
                for line in file:
                    data=line.split(":")
                    if data[3]=="expend":
                        aa+=int(data[2])
            with open("save/alert.txt", "r",encoding='utf-8') as file:
                for line in file:
                    data1 = line.split(":")
                    if str(now.month) == str(data1[0]):
                        num = data1[1].split('/')
                        sum += int(num[0])
            if sum==0:
                self.textBrowser.setPlainText("아직 한도 금액이 없습니다.")
            else:
                self.textBrowser.setPlainText(
                    "현재 이번달 총 이용금액은 " + str(aa) + "원이고 " + "한도 금액에 {:.2f}%만큼 사용했습니다".format((aa / sum)*100.0))

        except FileNotFoundError:
            pass


    def mfunc3(self):
        aa = 0
        sum=0
        try:
            with open("save/data" + str(now.month)+".txt", "r",encoding='utf-8') as file:
                for line in file:
                    data=line.split(":")
                    if data[3]=="expend":
                        aa+=int(data[2])
        except FileNotFoundError:
            pass
        with open("save/alert.txt", "r",encoding='utf-8') as file:
            for line in file:
                data1 = line.split(":")
                if str(now.month)==str(data1[0]):
                    num=data1[1].split('/')
                    sum+=int(num[0])
        if aa>=sum:
            self.msg.setWindowTitle('alert')
            self.msg.setText('한도량을 초과 사용했습니다.')
            self.msg.show()

            return 1
        elif aa>=sum/10*9:
            self.msg.setWindowTitle('alert')
            self.msg.setText('한도량의 9/10를 사용했습니다.')
            self.msg.show()
            return 2

        elif aa>=sum/4*3:
            self.msg.setWindowTitle('alert')
            self.msg.setText('한도량의 3/4를 사용했습니다.')
            self.msg.show()
            return 3


    def func2(self):
        sum=0
        try:
            with open("save/data" + str(now.month-1) + ".txt", "r",encoding='utf-8') as file:
                for line in file:
                    dataU=line.split(":")
                    if dataU[3]=="expend":
                        sum+=int(dataU[2])
            self.label.setText(str(sum))
        except:
            self.label.setText("no data")
        try:
            sum=0
            with open("save/alert" + ".txt", "r",encoding='utf-8') as file:
                for line in file:
                    data1 = line.split(":")
                    if str(now.month) == str(data1[0]):
                        num = data1[1].split('/')
                        sum += int(num[0])
            self.label_4.setText(str(now.month)+"월달 한도:" )
            self.label_5.setText(str(sum))

        except:
            self.label_4.setText(str(now.month) + "월달 한도:")
            self.label_5.setText("no data")
    def clear(self):
        with open("save/alert" + ".txt", "w",encoding='utf-8') as file:
            file.write("")

        self.func2()

    def inputdata(self):
        try:
            if self.num1.text() != str(0):
                bb = int(self.num1.text())

                with open("save/alert" + ".txt", "a",encoding='utf-8') as file:
                    file.write(str(now.month) + ":")
                    file.write(str(bb) + "\n")
            else:
                print("0원은 입력이 불가합니다")
                self.Home()

        except ValueError:
            print("숫자를 입력하세요")
            self.Home()

    def Home(self):
        self.close()
