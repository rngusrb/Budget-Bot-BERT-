from PyQt6.QtWidgets import *
import pandas as pd
from PyQt6 import uic
from datetime import datetime
now=datetime.now()
form_savemoney=uic.loadUiType("ui/savemoney.ui")[0]


class savemoney(QDialog, QWidget, form_savemoney):
    def __init__(self):
        super(savemoney, self).__init__()
        self.initUI()
        self.show()
        self.num5=0
        self.useMdata = [0, 0, 0, 0, 0]
        self.loadmonth()

    def initUI(self):
        self.setupUi(self)
        self.okay.clicked.connect(self.Home)
        self.pushButton.clicked.connect(self.makesub)
        self.pushButton.clicked.connect(self.makedata)


    def makesub(self):
        self.num5=self.lineEdit_2.text()

    def loadmonth(self):
        sum=0
        with open("save/data"+str(now.month-1)+".txt","r",encoding="utf-8") as file:
            for line in file:
                usedata=line.split(":")
                if usedata[3]=="expend":
                    sum=sum+int(usedata[2])
                    if usedata[4]=="식사\n":
                        self.useMdata[0]=int(self.useMdata[0])+int(usedata[2])
                    elif usedata[4]=="건강\n":
                        self.useMdata[1]=int(self.useMdata[1])+int(usedata[2])
                    elif usedata[4]=="마트/편의점\n":
                        self.useMdata[2]=int(self.useMdata[2])+int(usedata[2])
                    elif usedata[4]=="교통\n":
                        self.useMdata[3]=int(self.useMdata[3])+int(usedata[2])
                    elif usedata[4]=="기타\n":
                        self.useMdata[4]=int(self.useMdata[4])+int(usedata[2])
        self.label_5.setText(str(sum))

    def makedata(self):
        dish = []
        health = []
        mart = []
        trafic = []
        etc = []
        for i in range(1, 13):
            try:
                with open("save/data" + str(i) + ".txt", "r",encoding="utf-8") as file:
                    for line in file:
                        dateD = line.split(":")
                        if dateD[3] == 'expend':
                            if dateD[4] == '식사\n':
                                dish.append(int(dateD[2]))
                            elif dateD[4] == '건강\n':
                                health.append(int(dateD[2]))
                            elif dateD[4] == '마트/편의점\n':
                                mart.append(int(dateD[2]))
                            elif dateD[4] == '교통\n':
                                trafic.append(int(dateD[2]))
                            elif dateD[4] == '기타\n':
                                etc.append(int(dateD[2]))
            except FileNotFoundError as e1:
                pass

        data1 = pd.read_csv("save/man2.csv", encoding='cp949', names=["1", "2", "3", "4", "5", "6", "7", "8"])
        data_list = data1.values.tolist()
        val = self.lineEdit.text()
        uselist = []
        for line in data_list:
            if int(val) <= 39:
                if line[0] == "39세이하가구":
                    uselist.append(line)
            elif 40 <= int(val) <= 49:
                if line[0] == "40~49세가구":
                    uselist.append(line)
            elif 50 <= int(val) <= 59:
                if line[0] == "50~59세가구":
                    uselist.append(line)
            elif 60 <= int(val):
                if line[0] == "60세이상 가구":
                    uselist.append(line)
        aa = 0
        bb = 0
        cc = 0
        dd = 0
        ee = 0
        for line in range(len(uselist)):
            if line == 5 or line == 15:
                aa += int(uselist[line][3])
            elif line == 11:
                bb += int(uselist[line][3])
            elif line == 9:
                cc += int(uselist[line][3])
            elif line == 10:
                dd += int(uselist[line][3])
            elif line == 6 or line == 7 or line == 13 or line == 16:
                ee += int(uselist[line][3])
        usersum = sum(dish) + sum(health) + sum(mart) + sum(trafic) + sum(etc)
        use = [aa, bb, cc, dd, ee]
        use2 = [sum(dish), sum(health), sum(mart), sum(trafic), sum(etc)]
        for i in range(len(use2)):
            if use2[i] != 0:
                use2[i] = use2[i] / usersum
            else:
                use[i] = 0
        consum = sum(use)
        use3 = [use[0] / consum, use[1] / consum, use[2] / consum, use[3] / consum, use[4] / consum]
        supersum = []
        for i in range(5):
            supersum.append(use2[i] - use3[i])
        for i in range(5):
            if supersum[i] <= 0:
                supersum[i] = 0
        sum1 = sum(supersum)
        for i in range(5):
            supersum[i] = round(supersum[i] / sum1, 2) * 100
        record = []
        uu = ["식사", '건강', '마트/편의점', '교통', '기타']
        for i in range(5):
            supersum[i] = int(supersum[i]) * int(self.num5) / 100
            if supersum[i] != 0:
                record.append(i)

        see = [0, 0, 0, 0, 0]
        aa = 5
        for i in range(5):
            if supersum[i] >= self.useMdata[i] * 5 / 10:
                supersum[i] = round(self.useMdata[i] * 5 / 10, 1)
                see[i] = 1
                aa -= 1
        sum3 = sum(supersum)
        mnum = (int(self.num5) - sum3) / aa
        if mnum > 0.1:
            for i in range(5):
                if see[i] == 0:
                    if self.useMdata[i] * 5 / 10 >= mnum:
                        supersum[i] = mnum
                    else:
                        supersum[i] = self.useMdata[i] * 5 / 10
            sum3 = sum(supersum)
            mnum = (int(self.num5) - sum3) / 5
        if mnum > 0.1:
            for i in range(5):
                supersum[i] = supersum[i] + mnum
        newrecord = []
        for i in range(5):
            if supersum[i] != 0:
                newrecord.append(i)

        self.textBrowser.setPlainText("다른 사람에 비해")
        ustr = ''
        for i in range(len(record)):
            if i == len(record) - 1:
                ustr += (str(uu[record[i]]))
            else:
                ustr += (str(uu[record[i]]) + ",")
        self.textBrowser.append(ustr)

        self.textBrowser.append("영역에서 평균 사용량이 많습니다.\n\n\n" + "추천하는 절약 금액으로는")
        for i in range(len(newrecord)):
            if i == len(newrecord) - 1:
                self.textBrowser.append(str(uu[newrecord[i]]) + " 영역에서 ")
                text = '<div style="color: red; display:inline-block;">' + str(
                    int(supersum[newrecord[i]])) + '</div>' + "원 만큼"
                self.textBrowser.append(text)


            else:
                self.textBrowser.append(str(uu[newrecord[i]]) + " 영역에서 ")
                text = '<div style="color: red; display:inline-block;">' + str(
                    int(supersum[newrecord[i]])) + '</div>' + "원"
                self.textBrowser.append(text)
        self.textBrowser.append("절약하는 것을 추천 드립니다.")


    def Home(self):
        self.close()