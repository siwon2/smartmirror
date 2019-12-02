# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'notification.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(QtCore.QObject):
    noti_List = []
    widget_List = []
    noti_Widget_List = []
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(500, 300)
        Form.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.noti1 = QtWidgets.QFrame(Form)
        self.noti1.setGeometry(QtCore.QRect(5, 5, 490, 90))
        self.noti1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.noti1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.noti1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.noti1.setObjectName("noti1")
        self.label = QtWidgets.QLabel(self.noti1)
        self.label.setGeometry(QtCore.QRect(10, 5, 60, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lbl_tag_1 = QtWidgets.QLabel(self.noti1)
        self.lbl_tag_1.setGeometry(QtCore.QRect(90, 5, 350, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_tag_1.setFont(font)
        self.lbl_tag_1.setObjectName("lbl_tag_1")
        self.lbl_message_1 = QtWidgets.QLabel(self.noti1)
        self.lbl_message_1.setGeometry(QtCore.QRect(5, 50, 470, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_message_1.setFont(font)
        self.lbl_message_1.setObjectName("lbl_message_1")
        self.noti2 = QtWidgets.QFrame(Form)
        self.noti2.setGeometry(QtCore.QRect(5, 105, 490, 90))
        self.noti2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.noti2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.noti2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.noti2.setObjectName("noti2")
        self.label_2 = QtWidgets.QLabel(self.noti2)
        self.label_2.setGeometry(QtCore.QRect(10, 5, 60, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lbl_tag_2 = QtWidgets.QLabel(self.noti2)
        self.lbl_tag_2.setGeometry(QtCore.QRect(90, 5, 350, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_tag_2.setFont(font)
        self.lbl_tag_2.setObjectName("lbl_tag_2")
        self.lbl_message_2 = QtWidgets.QLabel(self.noti2)
        self.lbl_message_2.setGeometry(QtCore.QRect(5, 50, 470, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_message_2.setFont(font)
        self.lbl_message_2.setObjectName("lbl_message_2")
        self.noti3 = QtWidgets.QFrame(Form)
        self.noti3.setGeometry(QtCore.QRect(5, 205, 490, 90))
        self.noti3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.noti3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.noti3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.noti3.setObjectName("noti3")
        self.label_3 = QtWidgets.QLabel(self.noti3)
        self.label_3.setGeometry(QtCore.QRect(10, 5, 60, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lbl_tag_3 = QtWidgets.QLabel(self.noti3)
        self.lbl_tag_3.setGeometry(QtCore.QRect(90, 5, 350, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_tag_3.setFont(font)
        self.lbl_tag_3.setObjectName("lbl_tag_3")
        self.lbl_message_3 = QtWidgets.QLabel(self.noti3)
        self.lbl_message_3.setGeometry(QtCore.QRect(5, 50, 470, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_message_3.setFont(font)
        self.lbl_message_3.setObjectName("lbl_message_3")

        self.noti_Widget_List = [[self.noti1, self.lbl_tag_1, self.lbl_message_1],
                                    [self.noti2, self.lbl_tag_2, self.lbl_message_2],
                                    [self.noti3, self.lbl_tag_3, self.lbl_message_3]]

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "알림"))
        self.lbl_tag_1.setText(_translate("Form", "tag"))
        self.lbl_message_1.setText(_translate("Form", "Message"))
        self.label_2.setText(_translate("Form", "알림"))
        self.lbl_tag_2.setText(_translate("Form", "tag"))
        self.lbl_message_2.setText(_translate("Form", "Message"))
        self.label_3.setText(_translate("Form", "알림"))
        self.lbl_tag_3.setText(_translate("Form", "tag"))
        self.lbl_message_3.setText(_translate("Form", "Message"))


    @QtCore.pyqtSlot()
    def displayNoti(self):
        if(len(self.noti_List) > 0):
            for i in range(len(self.noti_List)):
                if(i > 2):
                    break
                
                self.noti_Widget_List[i][1].setText(self.noti_List[i]["tag"])
                self.noti_Widget_List[i][2].setText(self.noti_List[i]["message"])
                self.noti_Widget_List[i][0].setVisible(True)

            if(len(self.noti_List) <= 3):
                for i in range(0, 3 - (len(self.noti_List))):
                    self.noti_Widget_List[2 - i][0].setVisible(False)
        else:
            self.noti_Widget_List[0][0].hide()

            

    @QtCore.pyqtSlot(str, str, int)
    def addNoti(self, tag, message, time):
        self.noti_List.append({"tag" : tag, "message" : message, "time" : time})
        print('add noti')
    

    @QtCore.pyqtSlot()
    def removeNoti(self):
        if(len(self.noti_List) > 0):
            del self.noti_List[0]
