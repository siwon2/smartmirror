# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'weather.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 400)
        Form.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.weather_icon = QtWidgets.QLabel(Form)
        self.weather_icon.setGeometry(QtCore.QRect(125, 15, 150, 150))
        self.weather_icon.setText("")
        self.weather_icon.setObjectName("weather_icon")
        self.label_temperature = QtWidgets.QLabel(Form)
        self.label_temperature.setGeometry(QtCore.QRect(100, 190, 200, 60))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.label_temperature.setFont(font)
        self.label_temperature.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_temperature.setAlignment(QtCore.Qt.AlignCenter)
        self.label_temperature.setObjectName("label_temperature")
        self.label_weather = QtWidgets.QLabel(Form)
        self.label_weather.setGeometry(QtCore.QRect(100, 250, 200, 60))
        font = QtGui.QFont()
        font.setFamily("HY견고딕")
        font.setPointSize(28)
        self.label_weather.setFont(font)
        self.label_weather.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_weather.setAlignment(QtCore.Qt.AlignCenter)
        self.label_weather.setObjectName("label_weather")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_temperature.setText(_translate("Form", "18ºC"))
        self.label_weather.setText(_translate("Form", "구름 조금"))

