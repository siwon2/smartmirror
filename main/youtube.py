#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt5.QtGui import QPalette, QKeySequence, QIcon
from PyQt5.QtCore import QDir, Qt, QUrl, QSize, QPoint, QTime, QMimeData, QProcess, pyqtSlot
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer, QMediaMetaData
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import (QApplication, QFileDialog, QHBoxLayout, QLineEdit,
                            QPushButton, QSizePolicy, QSlider, QMessageBox, QStyle, QVBoxLayout,  
                            QWidget, QShortcut, QMenu)
import sys
import os
import subprocess

import yapi
#QT_DEBUG_PLUGINS

class VideoPlayer(QWidget):
    video_url = "https://www.youtube.com/watch?v=xT2gqqFlNQQ" #youtube video url

    def __init__(self, aPath, parent=None):
        super(VideoPlayer, self).__init__(parent)

        self.setAttribute( Qt.WA_NoSystemBackground, True )
        self.setAcceptDrops(True)

        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.StreamPlayback)
        self.mediaPlayer.mediaStatusChanged.connect(self.printMediaData)
        self.mediaPlayer.setVolume(80)

        self.videoWidget = QVideoWidget(self)

        self.clip = QApplication.clipboard()
        self.process = QProcess(self)
        self.process.readyRead.connect(self.dataReady)
#        self.process.started.connect(lambda: print("grabbing YouTube URL"))
        self.process.finished.connect(self.playFromURL)

        self.myurl = ""
        
        controlLayout = QHBoxLayout()
        controlLayout.setContentsMargins(5, 0, 5, 0)

        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.videoWidget)
        layout.addLayout(controlLayout)

        self.setLayout(layout)
        
        self.myinfo = "©2016\nAxel Schneider\n\nMouse Wheel = Zoom\nUP = Volume Up\nDOWN = Volume Down\n" + \
                "LEFT = < 1 Minute\nRIGHT = > 1 Minute\n" + \
                "SHIFT+LEFT = < 10 Minutes\nSHIFT+RIGHT = > 10 Minutes"

        self.widescreen = True

        self.mediaPlayer.setVideoOutput(self.videoWidget)
        self.mediaPlayer.error.connect(self.handleError)

        print("QT5 Player started")
        self.suspend_screensaver()

    
    def playFromURL(self):
        self.mediaPlayer.pause()
        self.myurl = self.clip.text()
        self.mediaPlayer.setMedia(QMediaContent(QUrl(self.myurl)))
        self.mediaPlayer.play()
        print(self.myurl)
    @pyqtSlot()
    def getYTUrl(self):
        # cmd = "youtube-dl -g -f best " + self.clip.text()
        cmd = "youtube-dl -g -f best " + self.video_url
        #print('cmd:',cmd)
        print("url:", self.video_url)
        self.process.start(cmd)
        self.show()

    def dataReady(self):
        self.myurl = str(self.process.readAll(), encoding = 'utf8').rstrip() ###
        self.myurl = self.myurl.partition("\n")[0]
        print(self.myurl)
        self.clip.setText(self.myurl)
        self.playFromURL()

    def suspend_screensaver(self):
        'suspend linux screensaver'
        proc = subprocess.Popen('gsettings set org.gnome.desktop.screensaver idle-activation-enabled false', shell=True)
        proc.wait()

    def resume_screensaver(self):
        'resume linux screensaver'
        proc = subprocess.Popen('gsettings set org.gnome.desktop.screensaver idle-activation-enabled true', shell=True)
        proc.wait()

    def play(self):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.mediaPlayer.pause()
        else:
            self.mediaPlayer.play()
    
    def setPosition(self, position):
        self.mediaPlayer.setPosition(position)

    def handleError(self):
        # self.playButton.setEnabled(False)
        self.mediaPlayer.stop()
        print("Error: ", self.mediaPlayer.error())

    def handleQuit(self):
        self.mediaPlayer.stop()
        self.resume_screensaver()
        print("Goodbye ...")
        app.quit()
        
    def mouseMoveEvent(self, event):   
        if event.buttons() == Qt.LeftButton:
            self.move(event.globalPos() \
                        - QPoint(self.frameGeometry().width() / 2, \
                        self.frameGeometry().height() / 2))
            event.accept() 
        
    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        elif event.mimeData().hasText():
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        if event.mimeData().hasUrls():
            f = str(event.mimeData().urls()[0].toLocalFile())
            self.loadFilm(f)
        elif event.mimeData().hasText():
            mydrop = str(event.mimeData().text())
            print(mydrop)
            ### YouTube url
            if "https://www.youtube" in mydrop:
                print("is YouTube")
#                mydrop = mydrop.partition("&")[0].replace("watch?v=", "v/")
                self.clip.setText(mydrop)
                self.getYTUrl()
            else:
                ### normal url
                self.mediaPlayer.setMedia(QMediaContent(QUrl(mydrop)))
                self.mediaPlayer.play()
            print(mydrop)
    
    def loadFilm(self, f):
            self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(f)))
            self.mediaPlayer.play()

    def printMediaData(self):
        if self.mediaPlayer.mediaStatus() == 6:
            if self.mediaPlayer.isMetaDataAvailable():
                res = str(self.mediaPlayer.metaData("Resolution")).partition("PyQt5.QtCore.QSize(")[2].replace(", ", " x ").replace(")", "")
                print("%s%s" % ("Video Resolution = ",res))
            else:
                print("no metaData available")

    @pyqtSlot(str)
    def setVidUrl(self, url):
        self.video_url = url

def stylesheet(self):
    return """
QSlider::handle:horizontal 
{
background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #333, stop:1 #555555);
width: 14px;
border-radius: 0px;
}
QSlider::groove:horizontal {
border: 1px solid #444;
height: 10px;
background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #000, stop:1 #222222);
}
QLineEdit
{
background: black;
color: #585858;
border: 0px solid #076100;
font-size: 8pt;
font-weight: bold;
}
    """

class Searcher():
    def __init__(self):
        self.api = yapi.YoutubeAPI('Youtube_data_api_v3_key')

    def search(self, name, resultCount=5):
        results = self.api.general_search(name, max_results=resultCount)
        return results


    
