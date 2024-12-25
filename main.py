import sys
from PyQt6.QtWidgets import *
from PyQt6 import uic
from thirdwindow import thirdwindow
from secondwindow import secondwindow
from amoney import amoney
from graph import forthWindow
from fix import Fixfee
from save import save
from savemoney import savemoney
form_class=uic.loadUiType("ui/main.ui")[0]
class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.calendar.clicked.connect(self.has_data)
        self.pushbutton1=QPushButton("데이터 보기")
        self.pushbutton2 = QPushButton("데이터 추가")
        self.b1.clicked.connect(self.Graph)
        self.pushbutton1.clicked.connect(self.thirdwin)
        self.pushbutton2.clicked.connect(self.button_second)
        self.am1.clicked.connect(self.button_am)
        self.fix.clicked.connect(self.fixwin)
        self.b1_3.clicked.connect(self.savewin)
        self.pushButton_3.clicked.connect(self.button_sa)
        self.datevar1=0
        self.datevar2=0
        self.savedata=[]
        self.actbut2()
        self.space.hide()


    def actbut1(self,data1,data2):
        main_layout=QVBoxLayout(self.space)
        main_layout.addWidget(self.pushbutton)

    def actbut2(self):
        main_layout = QGridLayout(self.space)
        main_layout.addWidget(self.pushbutton1,0,0)
        main_layout.addWidget(self.pushbutton2,0,1)
    def button_second(self):
        print(self.datevar1,self.datevar2)
        self.second=secondwindow(self.datevar1,self.datevar2)
        self.second.exec()
        self.show()
    def button_am(self):
        self.am=amoney()
        self.am.exec()
        self.show()
    def button_sa(self):
        self.sa=savemoney()
        self.sa.exec()
        self.show()
    def Graph(self):
        self.hide()
        self.graph=forthWindow()
        self.graph.exec()
        self.show()

    def thirdwin(self):
        self.third=thirdwindow(self.savedata)
        self.third.exec()
        self.show()
    def fixwin(self):
        self.third=Fixfee()
        self.third.exec()
        self.show()
    def savewin(self):
        self.third=save()
        self.third.exec()
        self.show()

    def has_data(self):
        self.space.hide()
        self.datevar1 = self.calendar.selectedDate().month()
        self.datevar2 = self.calendar.selectedDate().day()
        self.savedata=[]
        indata=0
        try:
            with open("save/data" + str(self.datevar1) + ".txt", "r",encoding='utf-8') as file:
                for line in file:
                    dateD=line.split(":")
                    if int(dateD[0])==self.datevar2:
                        self.savedata.append(line)
                        indata=1
                file.close()
            if indata==1:
                self.space.show()

            if indata==0:
                self.button_second()

        except FileNotFoundError as e1:
            self.button_second()

if __name__=="__main__":
    app=QApplication(sys.argv)
    myWindow=WindowClass()
    myWindow.show()
    app.exec()