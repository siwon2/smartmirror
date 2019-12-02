import json

from urllib import request
from urllib import parse

def getPlaceData(address, key):
    base_url = 'https://maps.googleapis.com/maps/api/place/textsearch/json?key=' + key
    query = '&query=' + parse.quote(address)
    sensor = '&sensor=false'
    
    url = base_url + query + sensor

    response = request.urlopen(url)
    raw_json = response.read()

    return json.loads(raw_json)

def getResult(data, idx):
    return data['results'][idx]

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

def getRouteData(startCoor, endCoor, key):
    base_url = "http://dev.virtualearth.net/REST/V1/Routes/Driving?"
    wp0 = "wp.0=" + str(startCoor['lat']) + ',' + str(startCoor['lng'])
    wp1 = "&wp.1=" + str(endCoor['lat']) + ',' + str(endCoor['lng'])
    key = "&key=" + key

    url = base_url + wp0 + wp1 + key

    response = request.urlopen(url)
    raw_json = response.read()

    return json.loads(raw_json)

def getDuration(data):
    duration = data['resourceSets'][0]['resources'][0]['travelDuration']
    unit = data['resourceSets'][0]['resources'][0]['durationUnit']

    return {"duration" : duration, "unit" : unit}

def getDistance(data):
    distance = data['resourceSets'][0]['resources'][0]['travelDistance']
    unit = data['resourceSets'][0]['resources'][0]['distanceUnit']

    return {"distance" : distance, "unit" : unit}

class mapClass():

    def __init__(
        self,
        BingMapAPIKey="AngatRrU3dqVA9KgVL2dR3dKFK0DEj1XsnQ9DbWmTndk0UnwoL054syEQRR5I6VQ",
        GoogleMapAPIKey="AIzaSyBbKYKniiu1TRXPCqTXlg32V2wbc19VN3o"
    ):
        
        self.BingAPIKey = BingMapAPIKey
        self.GoogleAPIKey = GoogleMapAPIKey

        self.wp0_rawdata = None
        self.wp1_rawdata = None
        self.route_rawdata = None

        self.wpData = None
        
    
    def search(self, wp0, wp1):

        self.wp0_rawdata = getPlaceData(wp0, self.GoogleAPIKey)
        self.wp1_rawdata = getPlaceData(wp1, self.GoogleAPIKey)

        wp0_size = getSize(self.wp0_rawdata)
        wp1_size = getSize(self.wp1_rawdata)

        wp0_address_list = []
        wp1_address_list = []

        for i in range(0, wp0_size):
            wp0_address_list.append(getAddress(self.wp0_rawData, i))

        for i in range(0, wp1_size):
            wp1_address_list.append(getAddress(self.wp1_rawData, i))

