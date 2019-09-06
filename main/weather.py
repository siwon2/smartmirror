import forecastio
import os

api_key = "darksky_api_key"

icons = {"bolt" : "weather_icons" + os.sep + "bolt.png",
         "clouds" : "weather_icons" + os.sep + "clouds.png",
         "cloudy_day" : "weather_icons" + os.sep + "cloudy_day.png",
         "drop" : "weather_icons" + os.sep + "drop.png",
         "snowflake" : "main" + os.sep + "weather_icons" + os.sep + "snowflake.png",
         "sun" : "weather_icons" + os.sep + "sun.png",
         "wind" : "weather_icons" + os.sep + "wind.png"}

def getWeatherInfo(lat, lng):

    forecast = forecastio.load_forecast(api_key, lat, lng)
    weather = forecast.currently()

    weather_status = weather.icon
    weather_icon = ""
    weather_text = ""

    if "partly-cloudy" in weather_status:
        weather_icon = icons["cloudy_day"]
        weather_text = "구름 조금"
    elif "clear" in weather_status:
        weather_icon = icons["sun"]
        weather_text = "맑음"
    elif "cloudy" in weather_status: 
        weather_icon = icons["clouds"]
        weather_text = "구름 많음"
    elif "fog" in weather_status:
        weather_icon = icons["clouds"]
        weather_text = "안개"
    elif "rain" in weather_status:
        weather_icon = icons["drop"]
        weather_text = "비"
    elif "snow" in weather_status:
        weather_icon = icons["snowflake"]
        weather_text = "눈"
    
    temperature = weather.temperature

    return weather_icon, temperature, weather_text