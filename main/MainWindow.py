from PyQt5 import QtCore, QtGui, QtWidgets

class Window(QtWidgets.QMainWindow):
    signal_notification_addNoti = QtCore.pyqtSignal(str, str, int)
    signal_notification_display = QtCore.pyqtSignal()
    signal_notification_remove = QtCore.pyqtSignal()

    signal_calendar_addCalendar = QtCore.pyqtSignal(str, str)
    signal_calendar_display = QtCore.pyqtSignal()
    signal_calendar_reset = QtCore.pyqtSignal()

    signal_youtube_setURL = QtCore.pyqtSignal(str)

    signal_addNoti = QtCore.pyqtSignal(str, str)
    signal_getuserText = QtCore.pyqtSignal(str)
    
    signal_addSchedule = QtCore.pyqtSignal(str)

    def __init__(self):
        super(Window, self).__init__()
    
    def initSignals(self, Ui_List):
        self.Ui_List = Ui_List

        self.signal_notification_addNoti.connect(Ui_List[3].addNoti)
        self.signal_notification_display.connect(Ui_List[3].displayNoti)
        self.signal_notification_remove.connect(Ui_List[3].removeNoti)

        # self.signal_calendar_addCalendar.connect(Ui_List[4].addCalendar)
        # self.signal_calendar_display.connect(Ui_List[4].displayCalendar)
        # self.signal_calendar_reset.connect(Ui_List[4].resetCalendar)

        self.signal_youtube_setURL.connect(Ui_List[5].setVidUrl)
        self.signal_addSchedule.connect(Ui_List[6].setSchedule)

    def getSignals(self):
        return [self.signal_notification_addNoti,
                self.signal_notification_display,
                self.signal_notification_remove,
                self.signal_calendar_addCalendar,
                self.signal_calendar_display,
                self.signal_calendar_reset,
                self.signal_addNoti,
                self.signal_getuserText,
                self.signal_youtube_setURL,
                self.signal_addSchedule
                ]
                
        
