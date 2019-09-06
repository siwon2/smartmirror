def weather_icon(self,MainWindow):
    while True:
        api_key = "6f2c1ebb5489c688baa2d4de29410089"

        #대구소프트웨어고등학교 위치
        lat = 35.663106 
        lng = 128.413759

        #서버 접속후 데이터를 받아옴
        forecast = forecastio.load_forecast(api_key, lat, lng)
        weather=forecast.currently()


        weather_cashe=weather.icon

        self.temperature.setText("[ %.1f ℃ ]" %(weather.temperature))
        
        if "day" in weather_cashe:
            if "partly-cloudy" in weather_cashe:
                self.weather.setPixmap(QtGui.QPixmap("D:\Python_Project\weather_icon\cloudy_day.png"))
            elif "cloudy" in weather_cashe:
                self.weather.setPixmap(QtGui.QPixmap("D:\Python_Project\weather_icon\clouds.png"))
            elif "clear" in weather_cashe:
                self.weather.setPixmap(QtGui.QPixmap("D:\Python_Project\weather_icon\sun.png"))

        elif "night" in weather_cashe:
            if "partly-cloudy" in weather_cashe:
                self.weather.setPixmap(QtGui.QPixmap("D:\Python_Project\weather_icon\cloudy_night.png"))
            elif "cloudy" in weather_cashe:
                self.weather.setPixmap(QtGui.QPixmap("D:\Python_Project\weather_icon\clouds.png"))
            elif "clear" in weather_cashe:
                self.weather.setPixmap(QtGui.QPixmap("D:\Python_Project\weather_icon\moon.png"))
        
        elif "cloudy" in weather_cashe or "fog" in weather_cashe:
            self.weather.setPixmap(QtGui.QPixmap("D:\Python_Project\weather_icon\clouds.png"))

        elif "rain" in weather_cashe:
            self.weather.setPixmap(QtGui.QPixmap("D:\Python_Project\weather_icon\drop.png"))

        elif "snow" in weather_cashe:
            self.weather.setPixmap(QtGui.QPixmap("D:\Python_Project\weather_icon\snowflake.png"))

        sleep(300)