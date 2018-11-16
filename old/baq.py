# Python 3
# Rethinking of the app using all JSON APIs
#
#import urllib.parse
import requests
import json
import datetime, socket
#
# Define the 'base' of the api requests, will later add on to these strings
#
# The AQI url needed is    url = 'http://www.airnowapi.org/aq/forecast/zipCode/?format=application/xml&zipCode=95818&date=2018-10-21&distance=1&API_KEY=F00    48A9B-16DA-4EA0-8CD1-0D651C9C05D9'
#
ymd = datetime.datetime.now()
timeout = 2200
socket.setdefaulttimeout(timeout)
#
# test values
#
station_id = ['Sacramento,CA','San Franciso,CA','Portland,OR','San Jose,CA']
lat = ['38.58','37.77', '45.52','37.39']
longit = ['-121.49','-122.38','-122.67','-122.08']
#
# grab and print tests
#
url='http://www.airnowapi.org/aq/forecast/latLong/?format=application/json&latitude='+lat[0]+'&longitude='+longit[0]+'&date='+ymd.strftime("%Y")+'-'+ymd    .strftime("%m")+'-'+ymd.strftime("%d")+'&distance=25&API_KEY=F0048A9B-16DA-4EA0-8CD1-0D651C9C05D9'
print(url)

json_data = requests.get(url).json()
print(json_data)
print()
beginAqi = "Air Quality "+(json_data[0]['Category']['Name'])
endAqi = "Air Quality "+(json_data[0]['Category']['Name'])

print(beginAqi)
print(endAqi)

print()

