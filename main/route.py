import Map
import math


def search(start, dest):
    startData = Map.getPlaceData(start)
    destData = Map.getPlaceData(dest)

    addr1 = Map.getAddress(startData, 0)
    addr2 = Map.getAddress(destData, 0)

    coor1 = Map.getCoordinates(startData, 0)
    coor2 = Map.getCoordinates(destData, 0)

    routeData = Map.getRouteData(coor1, coor2)
    if routeData is None:
        return "결과 없음", "결과 없음", 0, 0

    duration = Map.getDuration(routeData)
    distance = Map.getDistance(routeData)
    
    edit_duration = duration["duration"] / 60

    str_duration = str(math.ceil(edit_duration)) + " 분"
    str_distance = str(distance["distance"]) + " km"

    return str_duration, str_distance, addr1, addr2

