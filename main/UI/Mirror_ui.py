# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Mirror.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    # label, label_2, calendar, youtube, notifi, label_3, label_4, forecast, route, selector, schedule, facebook, kakaotalk
    widget_List = [
    ]
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1920, 1080)
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.widget_List.append(self.label)
        self.label.setGeometry(QtCore.QRect(2, 2, 550, 80))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.widget_List.append(self.label_2)
        self.label_2.setGeometry(QtCore.QRect(2, 84, 550, 80))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.widget_Calendar = QtWidgets.QWidget(self.centralwidget)
        self.widget_List.append(self.widget_Calendar)
        self.widget_Calendar.setGeometry(QtCore.QRect(2, 164, 500, 300))
        self.widget_Calendar.setStyleSheet("background-color: rgb(198, 198, 198);")
        self.widget_Calendar.setObjectName("widget_Calendar")
        self.widget_youtube = QtWidgets.QWidget(self.centralwidget)
        self.widget_List.append(self.widget_youtube)
        self.widget_youtube.setGeometry(QtCore.QRect(2, 464, 500, 300))
        self.widget_youtube.setStyleSheet("background-color: rgb(84, 84, 84);")
        self.widget_youtube.setObjectName("widget_youtube")
        self.widget_notification = QtWidgets.QWidget(self.centralwidget)
        self.widget_List.append(self.widget_notification)
        self.widget_notification.setGeometry(QtCore.QRect(2, 764, 500, 300))
        self.widget_notification.setStyleSheet("background-color: rgb(35, 35, 35);")
        self.widget_notification.setObjectName("widget_notification")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.widget_List.append(self.label_3)
        self.label_3.setGeometry(QtCore.QRect(1400, 2, 500, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.widget_List.append(self.label_4)
        self.label_4.setGeometry(QtCore.QRect(1400, 52, 500, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.widget_forecast = QtWidgets.QWidget(self.centralwidget)
        self.widget_List.append(self.widget_forecast)
        self.widget_forecast.setGeometry(QtCore.QRect(1510, 110, 400, 400))
        self.widget_forecast.setStyleSheet("background-color: rgb(172, 172, 172);\n"
"")
        self.widget_forecast.setObjectName("widget_forecast")
        self.widget_route = QtWidgets.QWidget(self.centralwidget)
        self.widget_List.append(self.widget_route)
        self.widget_route.setGeometry(QtCore.QRect(1360, 520, 550, 150))
        self.widget_route.setStyleSheet("background-color: rgb(124, 124, 124);")
        self.widget_route.setObjectName("widget_route")

        self.widget_selector = QtWidgets.QWidget(self.centralwidget)
        self.widget_List.append(self.widget_selector)
        self.widget_selector.setGeometry(QtCore.QRect(580, 370, 700, 470))
        self.widget_selector.setObjectName("widget_selector")

        self.widget_schedule = QtWidgets.QWidget(self.centralwidget)
        self.widget_List.append(self.widget_schedule)
        self.widget_schedule.setGeometry(QtCore.QRect(1360, 680, 550, 300))
        self.widget_schedule.setStyleSheet("background-color: rgb(94, 94, 94);")
        self.widget_schedule.setObjectName("widget_schedule")
        self.btn_kakaotalk = QtWidgets.QPushButton(self.centralwidget)
        self.widget_List.append(self.btn_kakaotalk)
        self.btn_kakaotalk.setGeometry(QtCore.QRect(1730, 990, 80, 80))
        self.btn_kakaotalk.setStyleSheet("image: url(:/button/facebook.jpg);")
        self.btn_kakaotalk.setText("")
        self.btn_kakaotalk.setObjectName("btn_kakaotalk")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "2019.07.15. Mon"))
        self.label_2.setText(_translate("MainWindow", "PM 19:08"))
        self.label_3.setText(_translate("MainWindow", "대구시 구지면"))
        self.label_4.setText(_translate("MainWindow", "23ºC"))

from UI import resource_rc
