# Python 3
# Rethinking of the app using all JSON APIs
#
#import urllib.parse
import requests
import json
#
# Define the 'base' of the api requests, will later add on to these strings
#
twilight_api = 'http://api.usno.navy.mil/rstt/oneday?date=today&loc='
#
# test values
#
station_id = ['Sacramento,CA','San Franciso,CA','Portland,OR','San Jose, CA']
lat = ['38.58','37.77', '45.52','37.39']
longit = ['-121.49','-122.38','-122.67','-122.08']
#
# grab and print tests
#
url = twilight_api + station_id[0]
print(url)

json_data = requests.get(url).json()
print(json_data)
print()
beginTwi = "Lights needed before "+(json_data['sundata'][0]['time'])[:10]
endTwi = "Lights needed after "+(json_data['sundata'][4]['time'])[:10]

print(beginTwi)
print(endTwi)

print()


#urllib.parse.urlencode({ hhttps://api.weather.gov/gridpoints/STO/52,67/forecast
