# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calendar.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(QtCore.QObject):
    # lbl_day1 ~ 6
    widget_List = []
    calendar_List = []
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(500, 300)
        Form.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.lbl_day1 = QtWidgets.QLabel(Form)
        self.lbl_day1.setGeometry(QtCore.QRect(5, 10, 490, 35))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_day1.setFont(font)
        self.lbl_day1.setStyleSheet("color: rgb(255, 255, 255);")
        self.lbl_day1.setObjectName("lbl_day1")
        self.widget_List.append(self.lbl_day1)
        self.lbl_day2 = QtWidgets.QLabel(Form)
        self.lbl_day2.setGeometry(QtCore.QRect(5, 55, 490, 35))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_day2.setFont(font)
        self.lbl_day2.setStyleSheet("color: rgb(255, 255, 255);")
        self.lbl_day2.setObjectName("lbl_day2")
        self.widget_List.append(self.lbl_day2)
        self.lbl_day3 = QtWidgets.QLabel(Form)
        self.lbl_day3.setGeometry(QtCore.QRect(5, 100, 490, 35))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_day3.setFont(font)
        self.lbl_day3.setStyleSheet("color: rgb(255, 255, 255);")
        self.lbl_day3.setObjectName("lbl_day3")
        self.widget_List.append(self.lbl_day3)
        self.lbl_day4 = QtWidgets.QLabel(Form)
        self.lbl_day4.setGeometry(QtCore.QRect(5, 145, 490, 35))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_day4.setFont(font)
        self.lbl_day4.setStyleSheet("color: rgb(255, 255, 255);")
        self.lbl_day4.setObjectName("lbl_day4")
        self.widget_List.append(self.lbl_day4)
        self.lbl_day5 = QtWidgets.QLabel(Form)
        self.lbl_day5.setGeometry(QtCore.QRect(5, 190, 490, 35))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_day5.setFont(font)
        self.lbl_day5.setStyleSheet("color: rgb(255, 255, 255);")
        self.lbl_day5.setObjectName("lbl_day5")
        self.widget_List.append(self.lbl_day5)
        self.lbl_day6 = QtWidgets.QLabel(Form)
        self.lbl_day6.setGeometry(QtCore.QRect(5, 235, 490, 35))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_day6.setFont(font)
        self.lbl_day6.setStyleSheet("color: rgb(255, 255, 255);")
        self.lbl_day6.setObjectName("lbl_day6")
        self.widget_List.append(self.lbl_day6)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.lbl_day1.setText(_translate("Form", "08/12 : 코딩하기 싫은 날"))
        self.lbl_day2.setText(_translate("Form", "08/13 : 코딩하기 싫은 날"))
        self.lbl_day3.setText(_translate("Form", "08/19 : 코딩하기 싫은 날"))
        self.lbl_day4.setText(_translate("Form", "08/26 : 코딩하기 싫은 날"))
        self.lbl_day5.setText(_translate("Form", "09/05 : 코딩하기 싫은 날"))
        self.lbl_day6.setText(_translate("Form", "12/22 : 코딩하기 싫은 날"))


    @QtCore.pyqtSlot(str, str)
    def addCalendar(self, date, summary):
        self.calendar_List.append([date, summary])

    @QtCore.pyqtSlot()
    def displayCalendar(self):
        for i in range(len(self.calendar_List)):
            string = self.calendar_List[i][0] + " : " + self.calendar_List[i][1]
            self.widget_List[i].setText(string)

    @QtCore.pyqtSlot()
    def resetCalendar(self):
        self.calendar_List.clear()
        for w in self.widget_List:
            w.setText("")

    

