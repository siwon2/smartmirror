import json

from urllib import request
from urllib import parse


bingMapsKey = "AngatRrU3dqVA9KgVL2dR3dKFK0DEj1XsnQ9DbWmTndk0UnwoL054syEQRR5I6VQ"
GoogleMapKey = "AIzaSyBbKYKniiu1TRXPCqTXlg32V2wbc19VN3o"

# google places api를 이용 address로 받아온 query를 검색해 data를 받아온뒤 dictionary 형태로 리턴
def getPlaceData(address):
    base_url = 'https://maps.googleapis.com/maps/api/place/textsearch/json?key=' + GoogleMapKey
    query = '&query=' + parse.quote(address)
    sensor = '&sensor=false'
    
    url = base_url + query + sensor

    response = request.urlopen(url)
    raw_json = response.read().decode('utf-8')

    return json.loads(raw_json)

# data에서 주소를 추출해 리턴
def getAddress(data, idx):
    return data['results'][idx]['formatted_address']

def getSize(data):
    return len(data['results'])

# data에서 좌표값(위도, 경도)를 추출해 리턴
def getCoordinates(data, idx, viewport="default"):
    if(viewport == "default"):
        return data['results'][idx]['geometry']['location']
    else:
        if(viewport == "northeast"):
            return data['results'][idx]['viewport']['northeast']
        if(viewport == "southwest"):
            return data['results'][idx]['viewport']['southwest']

def getRouteData(startCoor, endCoor):
    base_url = "http://dev.virtualearth.net/REST/V1/Routes/Driving?"
    wp0 = "wp.0=" + str(startCoor['lat']) + ',' + str(startCoor['lng'])
    wp1 = "&wp.1=" + str(endCoor['lat']) + ',' + str(endCoor['lng'])
    key = "&key=" + bingMapsKey

    url = base_url + wp0 + wp1 + key

    try:
        response = request.urlopen(url)
        raw_json = response.read().decode('utf-8')
    except urllib.error.HTTPError:
        return None

    return json.loads(raw_json)

def getDuration(data):
    duration = data['resourceSets'][0]['resources'][0]['travelDuration']
    unit = data['resourceSets'][0]['resources'][0]['durationUnit']

    return {"duration" : duration, "unit" : unit}

def getDistance(data):
    distance = data['resourceSets'][0]['resources'][0]['travelDistance']
    unit = data['resourceSets'][0]['resources'][0]['distanceUnit']

    return {"distance" : distance, "unit" : unit}


if __name__ == "__main__":
    start = "서울 63빌딩"
    end = "서울 국회의사당"

    data1 = getPlaceData(start)
    data2 = getPlaceData(end)

    #print(data2)

    coor1 = getCoordinates(data1, 0)
    coor2 = getCoordinates(data2, 0)
    #getDistanceData({"lat" : 35.8170201, "lng" : 128.523227}, {"lat" : 37.5318046, "lng" : 126.9141547})
    routedata = getRouteData(coor1, coor2)

    print(getDuration(routedata))
    print(getDistance(routedata))



