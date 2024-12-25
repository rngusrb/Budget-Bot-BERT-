import calendar
from datetime import datetime
from PyQt6.QtWidgets import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt6 import uic
import matplotlib.pyplot as plt
import pandas as pd

now=datetime.now()
form_forthWindow= uic.loadUiType("ui/test.ui")[0]

class forthWindow(QDialog,QWidget, form_forthWindow):

    def __init__(self):
        super(forthWindow, self).__init__()
        self.initUI()
        self.show()
        self.ddata()
        self.Mcirclev()
        self.month.setText(str(now.year)+'년 '+str(now.month)+"월")
        self.month_2.setText(str(now.year)+'년 '+str(now.month)+"월")
        self.label.setText(str(now.year) + '년' + str(self.pmonth)+"월의 " + "지출")


    def initUI(self):
        self.setupUi(self)
        self.rb2.clicked.connect(self.Home)
        self.db.setChecked(True)
        ''''''
        self.smonth = now.month
        self.data=[]
        self.fig = plt.Figure()
        self.canvas = FigureCanvas(self.fig)
        self.graph_verticalLayout.addWidget(self.canvas)
        self.prev.clicked.connect(self.Minus)
        self.prev.clicked.connect(self.Ymdcheck)
        self.next.clicked.connect(self.Plus)
        self.next.clicked.connect(self.Ymdcheck)
        self.db_3.clicked.connect(self.mdata)
        self.db.clicked.connect(self.ddata)
        '''원그래프'''
        self.cmonth = now.month
        self.ccmonth=now.month
        self.mb_2.setChecked(True)
        date = datetime(now.year, self.cmonth, 1)
        iso_calendar = date.isocalendar()
        week = iso_calendar[1]
        self.cweek=1
        self.cweek2=week
        self.cdata=[]
        self.fig1 = plt.Figure()
        self.canvas1 = FigureCanvas(self.fig1)
        self.graph_verticalLayout1.addWidget(self.canvas1)
        self.prev_2.clicked.connect(self.CMinus)
        self.prev_2.clicked.connect(self.CYmdcheck)
        self.next_2.clicked.connect(self.CPlus)
        self.next_2.clicked.connect(self.CYmdcheck)
        self.mb_2.clicked.connect(self.Mcirclev)
        self.db_2.clicked.connect(self.Ycirclev)
        self.Ycirclev()
        """현재 총 지출"""
        self.pmonth=now.month
        self.Prefee()
        self.prev_3.clicked.connect(self.PMinus)
        self.prev_3.clicked.connect(self.Prefee)
        self.next_3.clicked.connect(self.PPlus)
        self.next_3.clicked.connect(self.Prefee)

    def PMinus(self):
        self.pmonth=self.pmonth-1
        self.label.setText(str(now.year) + '년 ' + str(self.pmonth) +'월의 '+ "지출")

    def PPlus(self):
        self.pmonth=self.pmonth+1
        self.label.setText(str(now.year) + '년 ' + str(self.pmonth) +'월의 '+ "지출")

    def Prefee(self):
        self.textBrowser.clear()
        mfix=[]
        yfix=[]
        use=[]
        labels=[['식사',0],['교통',0],['마트/편의점',0],['건강',0],['교육',0],['주거/통신',0],['기타',0]]
        with open("save/fix" + ".txt", "r",encoding='utf-8') as file:
            for line in file:
                dateD = line.split(":")
                if dateD[0] == 'month':
                    mfix.append([dateD[1],dateD[2]])
                elif dateD[0] == 'year':
                    yfix.append([dateD[1], dateD[2]])
            file.close()
        sum=0
        try:
            with open("save/data" + str(self.pmonth) + ".txt", "r",encoding='utf-8') as file:
                for line in file:
                    dateD = line.split(":")
                    if dateD[3] == 'expend':
                        use.append([dateD[2], dateD[4]])
                file.close()
            for i in range(len(use)):
                for t in range(len(labels)):
                    if use[i][1] == labels[t][0] + '\n':
                        labels[t][1] += int(use[i][0])
                        sum = sum + int(use[i][0])
            string1="{:<5}: {:8d}   {:<5}: {:8d}   {:<5}: {:8d}\n{:<5}: {:8d}   {:<5}: {:8d}   {:<5}: {:8d}\n{:<5}: {:8d}".format(labels[0][0],labels[0][1],labels[1][0],labels[1][1],labels[2][0],labels[2][1],labels[3][0],labels[3][1],labels[4][0],labels[4][1],labels[5][0],labels[5][1],labels[6][0],labels[6][1])
            self.textBrowser.setPlainText(string1)
            '''labels[0][0] + ": " + str(labels[0][1]) + "   ," + labels[1][0] + ": " + str(labels[1][1]) + "   ," +
                labels[2][0] + ": " + str(labels[2][1]) + "\n" +
                labels[3][0] + ": " + str(labels[3][1]) + "   ," + labels[4][0] + ": " + str(labels[4][1]) + "   ," +
                labels[5][0] + ": " + str(labels[5][1]) + '\n' +
                labels[6][0] + ": " + str(labels[6][1])'''
        except FileNotFoundError:
            pass
        wtext = '월 고정 비용:'
        ytext = "년 고정 비용: "
        if len(mfix) != 0:
            for i in range(len(mfix)):
                sum = sum + int(mfix[i][1])
                if i == len(mfix) - 1:
                    wtext = wtext + ("  (" + mfix[i][0] + "/" + str(mfix[i][1]) + ")")
                else:
                    wtext = wtext + ("  (" + mfix[i][0] + "/" + str(mfix[i][1]) + "),")
        else:
            wtext = wtext + (' 없음')
        self.textBrowser.append(wtext)
        if len(yfix) != 0:
            for i in range(len(yfix)):
                sum = sum + round(int(yfix[i][1])/12)
                if i == len(yfix) - 1:
                    ytext = ytext + ("  (" + yfix[i][0] + "/" + str(yfix[i][1]) + ")")
                else:
                    ytext = ytext + ("  (" + yfix[i][0] + "/" + str(yfix[i][1]) + "),")
        else:
            ytext = ytext + (' 없음')
        self.textBrowser.append(ytext)
        self.textBrowser.append("총 지출 금액: " + str(sum))


    '''--------------------'''
    def Minus(self):
        self.smonth=self.smonth-1
        if self.db_3.isChecked():
            self.month.setText(str(now.year)+'년')
        else:
            self.month.setText(str(now.year) + '년 ' + str(self.smonth)+'월')


    def Plus(self):
        self.smonth=self.smonth+1
        if self.db_3.isChecked():
            self.month.setText(str(now.year)+'년')
        else:
            self.month.setText(str(now.year) + '년 ' + str(self.smonth)+"월")


    def Loaddata(self,month):
        num = month
        self.data = pd.read_csv('save/data' + str(num) + '.txt', sep=":", names=["날짜", "이용이름", "금액", "이용 방법","분야"], header=None,encoding='utf-8')

    def Ymdcheck(self):
        if self.db.isChecked():
            self.ddata()
        elif self.db_3.isChecked():
            self.mdata()

    def ddata(self):
        self.fig.clear()
        self.month.setText(str(now.year) + '년 ' + str(self.smonth) + "월")

        try:
            self.Loaddata(self.smonth)
        except FileNotFoundError:
            self.data= pd.read_csv( 'save/dummy.txt',sep=":", names=["날짜", "이용이름", "금액", "이용 방법","분야"], header=None,encoding='utf-8')
        view1 = []
        view2 = []
        for i in range(0, 32):
            data1 = self.data[(self.data["이용 방법"] == "expend") & (self.data["날짜"] == i)]
            sum = data1['금액'].sum()
            view1.append(sum)
        for i in range(0, 32):
            data1 = self.data[(self.data["이용 방법"] == "earn") & (self.data["날짜"] == i)]
            sum = data1['금액'].sum()
            view2.append(sum)
        aa=max(view1)
        x4=[aa/4,aa/2,aa*3/4,aa]
        x1 = []
        x2 = []
        x3 = []
        for i in range(0, 32):
            x1.append(i)
        for i in range(0, 32):
            x2.append(i + 0.5)
        for i in range(0, 32):
            x3.append(i + 0.2)
        gra = self.fig.add_subplot()
        gra.cla()
        gra.bar(x1, view1, width=0.4, color='r')
        gra.bar(x2, view2, width=0.4, color='g')
        gra.set_xticks(x3, labels=x1, fontsize=5)

        self.canvas.draw()

    def mdata(self):
        self.month.setText(str(now.year)+'년')

        self.fig.clear()
        mdata=[]
        mdata2=[]
        d=[1,2,3,4,5,6,7,8,9,10,11,12]
        for i in range(1, 13):
            try:
                self.Loaddata(i)
                data1 = self.data[(self.data["이용 방법"] == "expend")]
                data2 = self.data[(self.data["이용 방법"] == "earn")]
                sum1 = data1['금액'].sum()
                sum2= data2['금액'].sum()
                mdata.append([i, sum1])
                mdata2.append([i+0.4,sum2])
            except FileNotFoundError:
                mdata.append([i, 0, 0])
        md=pd.DataFrame(mdata)
        md2=pd.DataFrame(mdata2)
        gra = self.fig.add_subplot()
        gra.cla()
        gra.bar(md[0], md[1], width=0.4, color='r')
        gra.bar(md2[0], md2[1], width=0.4, color='g')
        gra.set_xticks(md[0],labels=d,fontsize=5)
        self.canvas.draw()

    '''--------------------'''
    def CLoaddata(self):
        self.fig1.clf()
        if  self.db_2.isChecked():
            num = self.cmonth
        elif self.mb_2.isChecked():
            num=self.ccmonth

        self.cdata = pd.read_csv('save/data' + str(num) + '.txt', sep=":", names=["날짜", "이용이름", "금액", "이용 방법","분야"], header=None,encoding='utf-8')

    def CPlus(self):
        if self.db_2.isChecked():
                self.cweek += 1
                self.cweek2 += 1
                date = datetime(now.year, self.cmonth+1, 1)
                iso_calendar = date.isocalendar()
                week = iso_calendar[1]
                ld = calendar.monthrange(now.year, self.cmonth)[1]
                date = datetime(now.year, self.cmonth, ld)
                iso_calendar = date.isocalendar()
                week1 = iso_calendar[1]
                date = datetime(now.year, self.cmonth, 1)
                iso_calendar = date.isocalendar()
                week2 = iso_calendar[1]
                mw=week1-week2+1
                if self.cweek2 == week+1:
                    self.cmonth+=1
                    self.cweek = 1
                    self.cweek2 -= 1



                elif self.cweek2==week and self.cweek==mw+1:
                    self.cmonth += 1
                    self.cweek =1



        elif self.mb_2.isChecked():
            self.ccmonth = self.ccmonth + 1
            self.month_2.setText(str(now.year) + '.' + str(self.ccmonth))

    def CMinus(self):
        if self.db_2.isChecked():
            self.cweek-=1
            self.cweek2-=1
            if self.cweek==0:
                self.cmonth-=1
                ld = calendar.monthrange(now.year, self.cmonth)[1]
                date = datetime(now.year, self.cmonth, ld)
                iso_calendar = date.isocalendar()
                week = iso_calendar[1]
                date1 = datetime(now.year, self.cmonth +1, 1)
                iso_calendar1 = date1.isocalendar()
                cweek2 = iso_calendar1[1]
                date = datetime(now.year, self.cmonth, 1)
                iso_calendar = date.isocalendar()
                week2 = iso_calendar[1]
                if cweek2==week:
                    self.cweek=week-week2+1
                    self.cweek2+=1
                else:
                    self.cweek = week - week2+1

        elif self.mb_2.isChecked():
            self.ccmonth = self.ccmonth - 1
            self.month_2.setText(str(now.year) + '.' + str(self.ccmonth))

    def CYmdcheck(self):
        if self.db_2.isChecked():
            self.Ycirclev()
        elif self.mb_2.isChecked():
            self.Mcirclev()

    def Mcirclev(self):
        self.month_2.setText(str(now.year) + '년 ' + str(self.ccmonth)+"월")
        try:
            self.CLoaddata()
            obj = ['식사', '교통', '마트/편의점', '건강', '교육', '주거/통신','기타']
            nlabel = ['meal', 'traffic', 'mart', 'health', 'edu','home','Etc']
            view1 = []
            d = self.cdata[(self.cdata["이용 방법"] == "expend")]
            ssum = d['금액'].sum()
            for i in range(1, 8):
                data1 = self.cdata[(self.cdata["이용 방법"] == "expend") & (self.cdata["분야"] == obj[i - 1])]
                sum = data1['금액'].sum()
                view1.append([obj[i - 1], sum / ssum * 100])
            view2 = []
            ulabel = []
            for i in range(0, 7):
                if view1[i][1] != 0.0:
                    view2.append(view1[i])
                    ulabel.append(nlabel[i])
            x1 = pd.DataFrame(view2)
            gra = self.fig1.add_subplot()
            gra.pie(x1[1], labels=ulabel, autopct='%.1f%%')
            self.canvas1.draw()
        except FileNotFoundError:
            gra = self.fig1.add_subplot()
            gra.pie([1], labels=['no data'], autopct='%.1f%%')
            self.canvas1.draw()

    def Ycirclev(self):
        self.month_2.setText(str(now.year) + '년 ' + str(self.cmonth) + '월 ' + str(self.cweek) + '주')
        try:
            self.CLoaddata()
            obj = ['식사', '교통', '마트/편의점', '건강', '교육', '주거/통신', '기타']
            nlabel = ['meal', 'traffic', 'mart', 'health', 'edu', 'home', 'Etc']
            view1 = []
            data1 = pd.DataFrame(columns=["날짜", "이용이름", "금액", "이용 방법", "분야"])
            last_day = calendar.monthrange(now.year, self.cmonth)[1]
            for i in range(1, last_day+1):
                m1 = datetime(now.year, self.cmonth, i)
                iso_calendar = m1.isocalendar()
                we = iso_calendar[1]
                if we == self.cweek2:
                    data2 = (self.cdata[(self.cdata["이용 방법"] == "expend") & (self.cdata["날짜"] == i)])
                    if data2.empty == False:
                        data1 = pd.concat([data1, data2])
            ssum = data1['금액'].sum()
            if ssum==0:
                gra = self.fig1.add_subplot()
                gra.pie([1], labels=['no data'], autopct='%.1f%%')
                self.canvas1.draw()
                raise FileNotFoundError
            for i in range(1, 8):
                data3 = data1[(data1["이용 방법"] == "expend") & (data1["분야"] == obj[i - 1])]
                sum = data3['금액'].sum()
                view1.append([obj[i - 1], sum / ssum * 100])
            view2 = []
            ulabel = []
            for i in range(0, 7):
                if view1[i][1] != 0.0:
                    view2.append(view1[i])
                    ulabel.append(nlabel[i])
            x1 = pd.DataFrame(view2)
            gra = self.fig1.add_subplot()
            gra.pie(x1[1], labels=ulabel, autopct='%.1f%%')
            self.canvas1.draw()
        except FileNotFoundError:
            gra = self.fig1.add_subplot()
            gra.pie([1], labels=['no data'], autopct='%.1f%%')
            self.canvas1.draw()


    def Home(self):
        self.close()
