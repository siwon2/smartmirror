from PyQt5 import QtWidgets,QtCore,QtGui
import sys, time
from PyQt5.QtCore import Qt,QUrl, pyqtSlot
from PyQt5 import QtWebKitWidgets
from PyQt5.QtWebKit import QWebSettings
import mouse

class window(QtWidgets.QWidget):
    vidUrl = "https://www.youtube.com/embed/Mq4AbdNsFVw"
    def __init__(self, parent=None):
        QWebSettings.globalSettings().setAttribute(QWebSettings.PluginsEnabled,True)
        super(window,self).__init__(parent)
        
        self.vlayout=QtWidgets.QVBoxLayout()

        self.webview=QtWebKitWidgets.QWebView()
        
        self.vlayout.addWidget(self.webview)
        
        self.setLayout(self.vlayout)
        self.resize(500,300)        
        self.show()
        
    @pyqtSlot(str)
    def setVidUrl(self, url):
        self.vidUrl = url+"?autoplay=1"
        print('url:',url)
        self.webview.setUrl(QUrl(self.vidUrl))