# Python 3
# Rethinking of the app using all JSON APIs
#
#import urllib.parse
import requests
import json
#
# Define the 'base' of the api requests, will later add on to these strings
#
wx_api = 'https://api.weather.gov/points/'
#
# test values
#
#nwslocation = 'STO/52,67/forecast/hourly'
#station_id = ['sac','SF','PDX','SV']
lat = ['38.58','37.77', '45.52','37.39']
longit = ['-121.49','-122.38','-122.67','-122.08']
#
# grab and print tests
#
print()
url = wx_api + lat[0]+','+longit[0]+'/forecast/hourly'
print(url)

json_data = requests.get(url).json()
print(json_data)
print()
print(json_data['properties']['periods'][3]['startTime'])
print()
ridein = json_data['properties']['periods'][2]['shortForecast'] + ', '\
    +json.dumps(json_data['properties']['periods'][2]['temperature'])      \
    +json_data['properties']['periods'][2]['temperatureUnit']  + ', wind '\
    +json_data['properties']['periods'][2]['windSpeed']        + ' from '\
    +json_data['properties']['periods'][2]['windDirection']
ridehome = json_data['properties']['periods'][10]['shortForecast'] + ', '\
    +json.dumps(json_data['properties']['periods'][10]['temperature'])      \
    +json_data['properties']['periods'][10]['temperatureUnit']  + ', wind '\
    +json_data['properties']['periods'][10]['windSpeed']        + ' from '\
    +json_data['properties']['periods'][10]['windDirection']
print(ridein)
print()
print(ridehome)
