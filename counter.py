import json
import urllib.request
from pyowm import OWM

class WeatherText(object):
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
        arr = self.toarr()
        for i in range(len(arr)):
            weather_type.append(arr[i]['WeatherText'])
        for i in weather_type:
            if i in nodups:
                continue
            else:
                nodups.append(i)
        return json.dumps(nodups)



