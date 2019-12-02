from PyQt5 import QtCore, QtGui

import Map
import time
import os
import math

import weather
import route
import Calendar

import gmail
import pharmacy
import facebook
import analyze
import analyst
import youtube

from google_api import player
from google_api import synthesizer
from google_api import mic_streamer



class STT(QtCore.QThread):

    def __init__(self, signal):
        super().__init__()

        self.signal = signal

    def run(self):
        from google.api_core.exceptions import OutOfRange
        while True:
            try:
                mic_streamer.stream((lambda text : self.signal.emit(text)))
            except OutOfRange:
                pass

#
# STT에서 받아온 결과를 처리하는 쓰레드
#
class Listener(QtCore.QThread):
    Ui_List = []
    signals = []
    
    lat = 0
    lng = 0
    addr = ""

    userText = ""


    keywords = {
        'route' : ['경로', '길', '에서', '까지'],
        'youtube' : ['유튜브', '영상'],
        'subway' : ['지하철', '역']            
    }

    onlyOneTime = True
    def __init__(self, Ui_List, signals):
        super().__init__()
        self.Ui_List = Ui_List
        self.signals = signals
        self.doctor = pharmacy.Pharmacy()

        self.signals[7].connect(self.readText)

        self.mic_listener = STT(self.signals[7])

        self.mic_listener.start()

        self.analyst = analyze.Analyst()

        self.youtubeSearcher = youtube.Searcher()

    def setCoor(self, lat, lng, addr):
        self.lat = lat
        self.lng = lng
        self.addr = addr 

    @QtCore.pyqtSlot(str)
    def readText(self, text):
        self.userText = text
        print(text)
        
    def run(self):
        while True:

            if self.userText is not "":
                d = analyze.Driver(self.analyst.analyze(self.userText))
                
                e = d.find_element({'real_write':analyze.Regex('미로야|미래야|밀어야|미러야|미뤄야|밀워야|미라야|밀아야|밀러야')})
                if e is not None:
                    d= e.after
                    print('after:')
                else:
                    
                    continue
                predicate = d.find_element({'역할':'서술어'},max_depth=1)
                
                if predicate is not None:
                    
                    # 경로 검색
          
                    if predicate.write == analyze.Regex(r'(검색하|알|가르치)\w+'):
                        elem =d.find_element({'조사들[]':{'write':analyze.Regex('에서|부터')}},1)
                        place_from = elem.before.real_write
                        print('출발지:',place_from)
                        place_to = elem.between({'조사들[]':{'write':analyze.Regex('로|까지')}},1).real_write
                        
                        print('도착지:',place_to)

                        duration, distance = route.search(place_from, place_to)
                        self.Ui_List[2].widget_List[0].setText(place_from)
                        self.Ui_List[2].widget_List[1].setText(place_to)
                        self.Ui_List[2].widget_List[2].setText(">")
                        self.Ui_List[2].widget_List[3].setText(duration)
                        self.Ui_List[2].widget_List[4].setText(distance)

                    
                    # 유튜브
                    if predicate.write == analyze.Regex(r'(틀|재생하)\w+'):
                        
                        elem = d.find_element({'write':'유튜브에서'})
                        search = elem.between(predicate).real_write
                        print('검색어:',search)
                        
                        #.items[0].id.kind == "youtube#videoId"
                        data = self.youtubeSearcher.search(search)
                        videoId = ""
                        
                        for item in data.items:
                            if item.id.kind == "youtube#video":
                                videoId = item.id.videoId
                                break           
                        
                        if videoId is not "":
                        
                            url = "https://youtube.com/embed/" + videoId
                            print('url:',url)
                            # 이 부분은 Linux에서만 실행이 되므로 원활한 코딩을 위해 잠시 막아놓았습니다.
                            self.signals[8].emit(url)
                        else:
                            str_noti = "검색하신 영상이 없는 것 같습니다"
                            audio_stream = synthesizer.synthesize_text(str_noti)
                            player.play_stream(audio_stream)
                        
                        
                    
                    # 약 추천
                    if predicate.write == analyze.Regex(r'(추천하)\w+'):
                        elem = d.find_element({'조사들[]':{'write':analyze.Regex('에|이')}},1)
                        symptom = elem.before.real_write

                        medicine = self.doctor.prescribe(symptom)
                        str_medicine = ""
                        if medicine is not None:
                            for m in medicine:
                                str_medicine += m + " "


                            str_prescribe = symptom + "에 추천 드리는 약은 " + str_medicine + " 입니다."
                            audio_stream = synthesizer.synthesize_text(str_prescribe)
                            player.play_stream(audio_stream)
                        else:
                            str_prescribe = "약에 대한 정보가 없거나 다시 말씀해 주세요"
                            audio_stream = synthesizer.synthesize_text(str_prescribe)
                            player.play_stream(audio_stream)
                
                self.userText = ""    

#
# 일정 시간마다 지속적인 업데이트가 필요한 함수를 위한 쓰레드
#
class Updater(QtCore.QThread):
    Ui_List = []
    signals = []
    
    weather_period = 3600
    time_period = 1
    noti_remove_period = 30
    noti_update_period = 10
    gmail_update_period = 600

    period_count = 0

    day = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    lat = 0
    lng = 0
    addr = ""

    need_calendar_update = True

    def __init__(self, Ui_List, signals):
        super().__init__()
        self.Ui_List = Ui_List
        self.signals = signals

        self.signals[6].connect(self.addNoti)

        self.f = facebook.FaceBook(signal=self.signals[6])
        self.f.login()
        self.f.register_handler(facebook.handler)
    
    def setCoor(self, lat, lng, addr):
        self.lat = lat
        self.lng = lng
        self.addr = addr 

        self.Ui_List[0].widget_List[5].setText(self.addr)

    def run(self):
        while True:
            if(self.period_count >= 360000):
                self.period_count = 0

            # 날씨정보 받아와서 UI에 띄워 주기 ( 3600초 간격 )
            if(self.period_count % self.weather_period == 0):
                icon, temperature, weather_text = weather.getWeatherInfo(self.lat, self.lng)

                pixmap = QtGui.QPixmap(os.path.abspath(icon))
                self.Ui_List[1].widget_List[0].setPixmap(pixmap)

                str1 = str(temperature) + u"ºC"
                self.Ui_List[1].widget_List[1].setText(str1)
                self.Ui_List[1].widget_List[2].setText(weather_text)


            # UI에 시간 띄우기 ( 1초 간격 ) , 구글 캘린더에서 일정 불러와야 하는지 확인 (0시 0분 마다)
            if(self.period_count % self.time_period == 0):
                now = time.localtime()
                str1 = time.strftime("%Y.%m.%d. ", now)
                str1 += self.day[now.tm_wday]

                str2 = "AM " + str(now.tm_hour)
                if(now.tm_hour / 12 > 1):
                    str2 = "PM " + str(now.tm_hour % 12)
                str2 += time.strftime(":%M:%S", now)
                self.Ui_List[0].widget_List[0].setText(str1)
                self.Ui_List[0].widget_List[1].setText(str2)

                self.today = time.strftime("%Y-%m-%d", now)

                if(now.tm_hour == 0 and now.tm_min == 0 and now.tm_sec == 0):
                    self.need_calendar_update = True


            # UI에 알림 띄우기 ( 10초 간격 ) 
            if(self.period_count % self.noti_update_period == 0):
                pass

            # 알림 삭제 ( 30초 간격 )
            if(self.period_count % self.noti_remove_period == 0):
                self.signals[2].emit()
                self.signals[1].emit()

            # 구글 캘린더에서 일정을 불러온 뒤 띄우기
            if(self.need_calendar_update):
                self.signals[5].emit()
                self.need_calendar_update = False
                calendars = Calendar.getCalendars()
                if calendars is not None:
                    for calendar in calendars:
                        date = calendar[0].split('T')[0]
                        summary = calendar[1]

                        self.signals[3].emit(date, summary)
                        if self.today == date:
                            self.signals[9].emit(summary)
                    
                    self.signals[4].emit()
            
            # gmail에서 읽지 않은 메일의 갯수를 받아온 뒤 띄워줍니다. ( 10분 간격 )
            if(self.period_count % self.gmail_update_period == 0):
                mailCount = gmail.getUnreadMail()
                tag = "Gmail"
                strMailCount = "읽지 않은 메일이 " + str(mailCount) + " 개 있습니다."
                self.addNoti(tag, strMailCount)


            time.sleep(1)
            self.period_count += 1
   
    @QtCore.pyqtSlot(str, str)
    def addNoti(self, tag, message):
        self.signals[0].emit(tag, message, self.period_count)
        self.signals[1].emit()
    


