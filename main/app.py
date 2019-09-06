from PyQt5 import QtCore, QtGui, QtWidgets
from UI import Mirror_ui
from UI import weather_ui
from UI import route_ui
from UI import notification_ui
from UI import calendar_ui
from UI import calendar_today_ui
from UI import youtube_ui

import sys

import MainWindow


#
# UI 초기화
#

# PyQt를 실행하기 위한 app을 만듭니다.
app = QtWidgets.QApplication(sys.argv)

# 메인 윈도우를 만듭니다.
mainWindow = MainWindow.Window()

# 프로그램에 쓰이는 모든 UI를 저장하는 리스트를 만듭니다.
Ui_List = []

# Main UI를 만든 뒤 메인 윈도우를 등록시켜 줍니다.
Main_Ui = Mirror_ui.Ui_MainWindow()
Main_Ui.setupUi(mainWindow)
# UI 리스트에 추가합니다.
Ui_List.append(Main_Ui)

# weather ui를 만든 뒤 위치에 등록시켜 줍니다.
Weather_Ui = weather_ui.Ui_Form()
Weather_Ui.setupUi(Main_Ui.widget_List[7])
# UI 리스트에 추가합니다.
Ui_List.append(Weather_Ui)

# route ui를 만든 뒤 위치에 등록시켜 줍니다.
Route_Ui = route_ui.Ui_Form()
Route_Ui.setupUi(Main_Ui.widget_List[8])
# UI 리스트에 추가합니다.
Ui_List.append(Route_Ui)

# notification ui를 만든 뒤 위치에 등록시켜 줍니다.
noti_Ui = notification_ui.Ui_Form()
noti_Ui.setupUi(Main_Ui.widget_List[4])
# UI 리스트에 추가합니다.
Ui_List.append(noti_Ui)

# calendar ui를 만든 뒤 위치에 등록시켜 줍니다.
calendar_Ui = calendar_ui.Ui_Form()
calendar_Ui.setupUi(Main_Ui.widget_List[2])
# UI 리스트에 추가합니다.
Ui_List.append(calendar_Ui)


# youtube ui를 만든 뒤 등록시켜 줍니다.
youtubePlayer = youtube_ui.window(Main_Ui.widget_List[3])
# UI 리스트에 추가합니다.
Ui_List.append(youtubePlayer)

calendar_today_Ui = calendar_today_ui.Ui_Form()
calendar_today_Ui.setupUi(Main_Ui.widget_List[10])
Ui_List.append(calendar_today_Ui)

# 쓰레드 간 통신을 위한 시그널을 설정해줍니다.
mainWindow.initSignals(Ui_List)

#
# 스마트 미러 초기화 시작
#
import os
import Map

# 현재 실행중인 경로를 받아옵니다.
PATH = os.getcwd()

# 위치 정보를 받을 변수를 미리 만들어 둡니다.
location = "서울"
loc_addr = "서울"
loc_coor = {}
loc_data = None

# 가져온 현재 위치를 Map api를 이용해 정보를 받아옵니다. (주소, 좌표)
loc_data = Map.getPlaceData(location)
loc_addr = Map.getAddress(loc_data, 0)
loc_coor = Map.getCoordinates(loc_data, 0)

#
# 스마트 미러 실행
#
mainWindow.showFullScreen()
mainWindow.show()
signals = mainWindow.getSignals()

#
# 백그라운드에서 동작하는 쓰레드를 실행합니다.
#
import Thread

updater = Thread.Updater(Ui_List, signals)
updater.setCoor(loc_coor['lat'], loc_coor['lng'], loc_addr)
updater.start()

Listener = Thread.Listener(Ui_List, signals)
Listener.setCoor(loc_coor['lat'], loc_coor['lng'], loc_addr)
Listener.start()

    
app.exec_()
updater.f.driver.quit()
sys.exit()
#sys.exit(app.exec_())

