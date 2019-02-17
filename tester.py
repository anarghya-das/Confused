import json
import urllib.request
from pyowm import OWM
API_KEY='106740011b0ccfb24c15328a94f6b7c9'
owm=OWM(API_KEY)
c=owm.weather_at_place("New York, New York")
c1=c.get_weather()
c2=c1.to_JSON
print(c2)
