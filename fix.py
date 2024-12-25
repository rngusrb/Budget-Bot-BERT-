from PyQt6.QtWidgets import *
from PyQt6 import uic
form_fixfee=uic.loadUiType("ui/fixfee.ui")[0]


class Fixfee(QDialog, QWidget, form_fixfee):
    def __init__(self):
        super(Fixfee, self).__init__()
        self.initUI()
        self.show()
        self.val1=0

    def initUI(self):
        self.setupUi(self)
        self.okay.clicked.connect(self.inputdata)
        self.okay.clicked.connect(self.Home)
        self.expend.clicked.connect(self.func)
        self.earn.clicked.connect(self.func2)

    def func(self):
        self.val1 = 1

    def func2(self):
        self.val1 = 2

    def inputdata(self):
        try:
            if self.amount.text() != str(0):
                    bb = int(self.amount.text())
                    with open("save/fix" + ".txt", "a",encoding='utf-8') as file:
                        if self.month.isChecked():
                            if self.val1 == 1:
                                file.write("month" + ":")
                                file.write(self.usingname.text() + ":")
                                file.write(self.amount.text() + ":")
                                file.write("expend" + ":")
                                file.write(self.ca.currentText() + "\n")
                                file.close()
                            elif self.val1 == 2:
                                file.write("month" + ":")
                                file.write(self.usingname.text() + ":")
                                file.write(self.amount.text() + ":")
                                file.write("earn" + ":")
                                file.write(self.ca.currentText() + "\n")
                                file.close()
                        elif self.year.isChecked():
                            if self.val1 == 1:
                                file.write("year" + ":")
                                file.write(self.usingname.text() + ":")
                                file.write(self.amount.text() + ":")
                                file.write("expend" + ":")
                                file.write(self.ca.currentText() + "\n")
                                file.close()
                            elif self.val1 == 2:
                                file.write("year" + ":")
                                file.write(self.usingname.text() + ":")
                                file.write(self.amount.text() + ":")
                                file.write("earn" + ":")
                                file.write(self.ca.currentText() + "\n")
                                file.close()

            else:
                print("0원은 입력이 불가합니다")
                self.Home()

        except ValueError:
            print("숫자를 입력하세요")
            self.Home()

    def Home(self):
        self.close()