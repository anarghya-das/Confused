import json
import urllib.request
from pyowm import OWM


class WeatherText(object):
    def __init__(self):
        self.mapper = {}

    def toarr(self):
        apiKey = "NMX2QYEuqSjNe8MBf6gE7uHoTSeu7KIB"
        results = 50  # 50,100,150
        contents = urllib.request.urlopen(
            "http://dataservice.accuweather.com/currentconditions/v1/topcities/" + str(
                results) + "?apikey=" + apiKey).read()
        arr = json.loads(contents)
        with open('cache.json', 'w') as f:
            f.write(json.dumps(arr))
        return arr

    def get_key(self):
        weather_type = []
        nodups = []
        ofmap = {}
        lon = {}
        lat = {}
        l = []
        arr = self.toarr()
        for i in range(len(arr)):
            lon.clear()
            lat.clear()
            l.clear()
            ofmap.clear()
            lon['Longitude'] = arr[i]['GeoPosition']['Longitude']
            lat['Latitude'] = arr[i]['GeoPosition']['Latitude']
            ofmap['Country'] = arr[i]['EnglishName']
            l.append(ofmap)
            l.append(lon)
            l.append(lat)
            print(l)
            self.mapper[arr[i]['WeatherText']] = l
            weather_type.append(arr[i]['WeatherText'])
        for i in weather_type:
            if i in nodups:
                continue
            else:
                nodups.append(i)
        return json.dumps(nodups)

    def getMapper(self):
        return self.mapper


obj = WeatherText()
print(obj.getMapper())
obj.get_key()
