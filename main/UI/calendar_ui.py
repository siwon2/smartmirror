# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calendar.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import time
import calendar
from datetime import date
from workalendar.asia import south_korea

class Ui_Form(object):

    day_list = []
    date_list = []

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(600, 450)
        Form.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.lbl_when = QtWidgets.QLabel(Form)
        self.lbl_when.setGeometry(QtCore.QRect(5, 5, 590, 35))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_when.setFont(font)
        self.lbl_when.setStyleSheet("color: rgb(255, 255, 255);")
        self.lbl_when.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_when.setObjectName("lbl_when")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(4, 45, 590, 450))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayoutWidget = QtWidgets.QWidget(self.frame)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 581, 401))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setHorizontalSpacing(7)
        self.gridLayout.setVerticalSpacing(5)
        self.gridLayout.setObjectName("gridLayout")
        self.day_15 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.day_15.setObjectName("day_15")
        self.gridLayout.addWidget(self.day_15, 3, 0, 1, 1)
        self.day_10 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.day_10.setObjectName("day_10")
        self.gridLayout.addWidget(self.day_10, 2, 2, 1, 1)
        self.day_22 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.day_22.setObjectName("day_22")
        self.gridLayout.addWidget(self.day_22, 4, 0, 1, 1)
        self.day_8 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.day_8.setObjectName("day_8")
        self.gridLayout.addWidget(self.day_8, 2, 0, 1, 1)
        self.day_29 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.day_29.setObjectName("day_29")
        self.gridLayout.addWidget(self.day_29, 5, 0, 1, 1)
        self.day_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.day_3.setStyleSheet("")
        self.day_3.setText("")
        self.day_3.setObjectName("day_3")
        self.gridLayout.addWidget(self.day_3, 1, 2, 1, 1)
        self.day_24 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.day_24.setObjectName("day_24")
        self.gridLayout.addWidget(self.day_24, 4, 2, 1, 1)
        self.day_17 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.day_17.setObjectName("day_17")
        self.gridLayout.addWidget(self.day_17, 3, 2, 1, 1)
        self.day_31 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.day_31.setObjectName("day_31")
        self.gridLayout.addWidget(self.day_31, 5, 2, 1, 1)
        self.day_35 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.day_35.setObjectName("day_35")
        self.gridLayout.addWidget(self.day_35, 5, 6, 1, 1)
        self.day_28 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.day_28.setObjectName("day_28")
        self.gridLayout.addWidget(self.day_28, 4, 6, 1, 1)
        self.day_14 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.day_14.setObjectName("day_14")
        self.gridLayout.addWidget(self.day_14, 2, 6, 1, 1)
        self.day_21 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.day_21.setObjectName("day_21")
        self.gridLayout.addWidget(self.day_21, 3, 6, 1, 1)
        self.day_7 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.day_7.setStyleSheet("")
        self.day_7.setText("")
        self.day_7.setObjectName("day_7")
        self.gridLayout.addWidget(self.day_7, 1, 6, 1, 1)
        self.day_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.day_2.setStyleSheet("")
        self.day_2.setText("")
        self.day_2.setObjectName("day_2")
        self.gridLayout.addWidget(self.day_2, 1, 1, 1, 1)
        self.lbl_sun = QtWidgets.QLabel(self.gridLayoutWidget)
        self.lbl_sun.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_sun.setObjectName("lbl_sun")
        self.gridLayout.addWidget(self.lbl_sun, 0, 0, 1, 1)
        self.day_1 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.day_1.setStyleSheet("")
        self.day_1.setText("")
        self.day_1.setObjectName("day_1")
        self.gridLayout.addWidget(self.day_1, 1, 0, 1, 1)
        self.lbl_mon = QtWidgets.QLabel(self.gridLayoutWidget)
        self.lbl_mon.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_mon.setObjectName("lbl_mon")
        self.gridLayout.addWidget(self.lbl_mon, 0, 1, 1, 1)
        self.lbl_tue = QtWidgets.QLabel(self.gridLayoutWidget)
        self.lbl_tue.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_tue.setObjectName("lbl_tue")
        self.gridLayout.addWidget(self.lbl_tue, 0, 2, 1, 1)
        self.lbl_wed = QtWidgets.QLabel(self.gridLayoutWidget)
        self.lbl_wed.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_wed.setObjectName("lbl_wed")
        self.gridLayout.addWidget(self.lbl_wed, 0, 3, 1, 1)
        self.lbl_sat = QtWidgets.QLabel(self.gridLayoutWidget)
        self.lbl_sat.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_sat.setObjectName("lbl_sat")
        self.gridLayout.addWidget(self.lbl_sat, 0, 6, 1, 1)
        self.day_23 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.day_23.setObjectName("day_23")
        self.gridLayout.addWidget(self.day_23, 4, 1, 1, 1)
        self.lbl_thu = QtWidgets.QLabel(self.gridLayoutWidget)
        self.lbl_thu.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_thu.setObjectName("lbl_thu")
        self.gridLayout.addWidget(self.lbl_thu, 0, 4, 1, 1)
        self.day_16 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.day_16.setObjectName("day_16")
        self.gridLayout.addWidget(self.day_16, 3, 1, 1, 1)
        self.lbl_fri = QtWidgets.QLabel(self.gridLayoutWidget)
        self.lbl_fri.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_fri.setObjectName("lbl_fri")
        self.gridLayout.addWidget(self.lbl_fri, 0, 5, 1, 1)
        self.day_30 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.day_30.setObjectName("day_30")
        self.gridLayout.addWidget(self.day_30, 5, 1, 1, 1)
        self.day_9 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.day_9.setObjectName("day_9")
        self.gridLayout.addWidget(self.day_9, 2, 1, 1, 1)
        self.day_26 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.day_26.setObjectName("day_26")
        self.gridLayout.addWidget(self.day_26, 4, 4, 1, 1)
        self.day_13 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.day_13.setObjectName("day_13")
        self.gridLayout.addWidget(self.day_13, 2, 5, 1, 1)
        self.day_33 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.day_33.setObjectName("day_33")
        self.gridLayout.addWidget(self.day_33, 5, 4, 1, 1)
        self.day_12 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.day_12.setObjectName("day_12")
        self.gridLayout.addWidget(self.day_12, 2, 4, 1, 1)
        self.day_19 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.day_19.setObjectName("day_19")
        self.gridLayout.addWidget(self.day_19, 3, 4, 1, 1)
        self.day_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.day_4.setStyleSheet("")
        self.day_4.setText("")
        self.day_4.setObjectName("day_4")
        self.gridLayout.addWidget(self.day_4, 1, 3, 1, 1)
        self.day_18 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.day_18.setObjectName("day_18")
        self.gridLayout.addWidget(self.day_18, 3, 3, 1, 1)
        self.day_32 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.day_32.setObjectName("day_32")
        self.gridLayout.addWidget(self.day_32, 5, 3, 1, 1)
        self.day_25 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.day_25.setObjectName("day_25")
        self.gridLayout.addWidget(self.day_25, 4, 3, 1, 1)
        self.day_11 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.day_11.setObjectName("day_11")
        self.gridLayout.addWidget(self.day_11, 2, 3, 1, 1)
        self.day_34 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.day_34.setObjectName("day_34")
        self.gridLayout.addWidget(self.day_34, 5, 5, 1, 1)
        self.day_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.day_5.setStyleSheet("")
        self.day_5.setText("")
        self.day_5.setObjectName("day_5")
        self.gridLayout.addWidget(self.day_5, 1, 4, 1, 1)
        self.day_20 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.day_20.setObjectName("day_20")
        self.gridLayout.addWidget(self.day_20, 3, 5, 1, 1)
        self.day_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.day_6.setStyleSheet("")
        self.day_6.setText("")
        self.day_6.setObjectName("day_6")
        self.gridLayout.addWidget(self.day_6, 1, 5, 1, 1)
        self.day_27 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.day_27.setObjectName("day_27")
        self.gridLayout.addWidget(self.day_27, 4, 5, 1, 1)
        self.day_36 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.day_36.setObjectName("day_36")
        self.gridLayout.addWidget(self.day_36, 6, 0, 1, 1)
        self.day_37 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.day_37.setObjectName("day_37")
        self.gridLayout.addWidget(self.day_37, 6, 1, 1, 1)
        self.day_38 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.day_38.setObjectName("day_38")
        self.gridLayout.addWidget(self.day_38, 6, 2, 1, 1)
        self.day_39 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.day_39.setObjectName("day_39")
        self.gridLayout.addWidget(self.day_39, 6, 3, 1, 1)
        self.day_40 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.day_40.setObjectName("day_40")
        self.gridLayout.addWidget(self.day_40, 6, 4, 1, 1)
        self.day_41 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.day_41.setObjectName("day_41")
        self.gridLayout.addWidget(self.day_41, 6, 5, 1, 1)
        self.day_42 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.day_42.setStyleSheet("")
        self.day_42.setObjectName("day_42")
        self.gridLayout.addWidget(self.day_42, 6, 6, 1, 1)
        self.gridLayout.setRowStretch(0, 1)
        self.gridLayout.setRowStretch(1, 2)
        self.gridLayout.setRowStretch(2, 2)
        self.gridLayout.setRowStretch(3, 2)
        self.gridLayout.setRowStretch(4, 2)
        self.gridLayout.setRowStretch(5, 2)
        self.gridLayout.setRowStretch(6, 2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.day_list = [self.lbl_sun, self.lbl_mon, self.lbl_tue, self.lbl_wed, self.lbl_thu,
                            self.lbl_fri, self.lbl_sat]

        self.date_list = [self.day_1, self.day_2, self.day_3, self.day_4, self.day_5, self.day_6,
                            self.day_7, self.day_8, self.day_9, self.day_10, self.day_11, self.day_12,
                            self.day_13, self.day_14, self.day_15, self.day_16, self.day_17, self.day_18,
                            self.day_19, self.day_20, self.day_21, self.day_22, self.day_23, self.day_24,
                            self.day_25, self.day_26, self.day_27, self.day_28, self.day_29, self.day_30,
                            self.day_31, self.day_32, self.day_33, self.day_34, self.day_35, self.day_36,
                            self.day_37, self.day_38, self.day_39, self.day_40, self.day_41, self.day_42]

        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)

        

        for i in range(len(self.day_list)):
            self.day_list[i].setStyleSheet("border: 1px solid white;\n"
                                                "color: white;")
            self.day_list[i].setFont(font)
            if i == 0:
                self.day_list[i].setStyleSheet("border: 1px solid white;\n"
                                                "color: red;")
            if i == 6:
                self.day_list[i].setStyleSheet("border: 1px solid white;\n"
                                                "color: skyblue;")

        for i in range(len(self.date_list)):
            self.date_list[i].setStyleSheet("border: 1px solid white;\n"
                                                "color: white;")
            self.date_list[i].setFont(font)
            
            if i % 7 == 0:
                self.date_list[i].setStyleSheet("border: 1px solid white;\n"
                                                "color: red;")
            if i % 7 == 6:
                self.date_list[i].setStyleSheet("border: 1px solid white;\n"
                                                "color: skyblue;")


        now = time.localtime()
        date_limit = calendar.monthrange(now.tm_year, now.tm_mon)

        day_first = date_limit[0] + 1
        if day_first == 7:
            day_first = 0

        day_last = date_limit[1]

        holi_cal = south_korea.SouthKorea()
        holidays = holi_cal.holidays(now.tm_year)
        

        for i in range(0, day_last):
            
            d = date(now.tm_year, now.tm_mon, i+1)

            if(holi_cal.is_holiday(d)):
                for i2, day in enumerate(holidays):
                    if day[0] == d:
                        self.date_list[day_first + i].setText(str(i+1) + "\n\n" + str(holidays[i2][1]))

                        self.date_list[day_first + i].setStyleSheet("border: 1px solid white;\n"
                                                                        "color: red;")
            else:
                self.date_list[day_first + i].setText(str(i+1) + "\n\n")

            
        
        self.lbl_when.setText(str(now.tm_year) + ". " + str(now.tm_mon))

        
            
        


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.lbl_when.setText(_translate("Form", "2019. 09"))
        self.lbl_sun.setText(_translate("Form", "Sun"))
        self.lbl_mon.setText(_translate("Form", "Mon"))
        self.lbl_tue.setText(_translate("Form", "Tue"))
        self.lbl_wed.setText(_translate("Form", "Wed"))
        self.lbl_sat.setText(_translate("Form", "Sat"))
        self.lbl_thu.setText(_translate("Form", "Thu"))
        self.lbl_fri.setText(_translate("Form", "Fri"))



if __name__ == "__main__":
    import sys
    # PyQt를 실행하기 위한 app을 만듭니다.
    app = QtWidgets.QApplication(sys.argv)

    # 메인 윈도우를 만듭니다.
    mainWindow = QtWidgets.QMainWindow()

    ui = Ui_Form()
    ui.setupUi(mainWindow)

    mainWindow.show()
    sys.exit(app.exec_())