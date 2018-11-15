#
#  Get the data needed from the APIs
#
import requests, json, datetime, socket,time
from sys import platform as _platform
#
timeout = 2800
socket.setdefaulttimeout(timeout)
#
# Define the cities considered
#
cities = ['Sacramento,CA','San Francisco,CA','Portland,OR','San Jose,CA']
#
# Define the latitude and longitude of the cities considered
#
lats = ['38.58','37.77', '45.52','37.39']
longits = ['-121.49','-122.38','-122.67','-122.08']
#
# Define additional data needed for APIs to work
#
ymd = datetime.datetime.now()
#
# Define the 'base' of the three api requests used, will later add on to these strings
#
url_wx = 'https://api.weather.gov/points/'
url_aqi='http://www.airnowapi.org/aq/forecast/latLong/?format=application/json&'
url_light = 'http://api.openweathermap.org/data/2.5/weather?'
#
# Functions to call individual APIs
#
#
# Function for basic weather data from the NWS
#
def get_wx(baseurl,lat,longit):
   "This function calls the basic weather data from NWS"
   url = baseurl + lat+','+longit+'/forecast/hourly' 
   r = requests.get(url)
   print(r)
   status = r.status_code
   if status != 200:
      time.sleep(300)
      r = requests.get(url)
      status = r.status_code
   if status != 200:
      time.sleep(300)
      r = requests.get(url)
      status = r.status_code
   if status != 200:
      print('No data after 3 tries') 
   try:
      print(status)
      json_data = r.json()
      #print(json_data)
      #json_data = requests.get(url).json()
      print(url)
      print()
      print(json_data['properties']['periods'][2]['startTime'])
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
   except:
      print(status)
      ridein = 'No weather data'
      ridehome = 'No weather data'
   print(ridein)
   print()
   print(ridehome)
   f.write(ridein+'\n')
   f.write(ridehome+'\n')
   # Create lists of data per city and ride time
   return
#
# Function for AQI from AirNow
#
def get_aqi(baseurl,lat,longit,ymd):
   "This function calls the AQI from AirNow"
   # Requires API Key
   if _platform == "linux" or _platform == "linux2":
       e = open('/home/dougdroplet2/projects/BikeWxX/BikeWxX/keys/AQIkey','r')
   elif _platform == "darwin":
       e = open('../bikewxxkeys/AQIkey','r') 
   elif _platform == "win32":
       print('create dir and continue')
   #
   url = baseurl + 'latitude='+lat+'&longitude='+longit+'&date='+ymd.strftime("%Y")+'-'+ymd.strftime("%m")+'-'+ymd.strftime("%d")+'&distance=25&API_KEY='+e.read().rstrip()
   print(url)
   e.close
   r = requests.get(url)
   print(r)
   status = r.status_code
   if status != 200:
      time.sleep(300)
      r = requests.get(url)
      status = r.status_code
   if status != 200:
      time.sleep(300)
      r = requests.get(url)
      status = r.status_code
   if status != 200:
      print('No data after 3 tries') 
   try:
      print(status)
      json_data = r.json()
      #print(json_data)
      # Always get the 0 data which is the AQI for this day, as there is only 1 forecast per day provided by the API
      rideinAqi = "Air Quality Index "+json.dumps(json_data[0]['AQI'])+"-"+(json_data[0]['Category']['Name'])
      ridehomeAqi = "Air Quality Index "+json.dumps(json_data[0]['AQI'])+"-"+(json_data[0]['Category']['Name'])
   except:
      rideinAqi = 'No air quality data'
      ridehomeAqi = 'No air quality data'
   print(rideinAqi)
   print(ridehomeAqi)
   f.write(rideinAqi+'\n') 
   f.write(ridehomeAqi+'\n') 
   print()
   return
#
# Function for twilight data from OpenWeather
#
def get_light(baseurl,lat,longit):
   "This function calls the twilight data from OpenWeather"
   # Requires API Key
   if _platform == "linux" or _platform == "linux2":
       g = open('/home/dougdroplet2/projects/BikeWxX/BikeWxX/keys/OWMkey','r')
   elif _platform == "darwin":
       g = open('../bikewxxkeys/OWMkey','r') 
   elif _platform == "win32":
       print('create dir and continue')
   #url = baseurl + city
   url = baseurl + 'lat='+lat+'&lon='+longit+'&APPID='+g.read().rstrip()
   g.close
   r = requests.get(url)
   print(r.url)
   status = r.status_code
   print(status)
   if status != 200:
      time.sleep(300)
      r = requests.get(url)
      status = r.status_code
   if status != 200:
      time.sleep(300)
      r = requests.get(url)
      status = r.status_code
   if status != 200:
      print('No data after 3 tries') 
   try:
      print(status)
      json_data = r.json()
      print(json_data)
      sunRise = json_data['sys']['sunrise']
      sunRise = time.strftime("%I:%M %p", time.localtime(sunRise))
      print(sunRise)
      sunSet = json_data['sys']['sunset']
      sunSet = time.strftime("%I:%M %p", time.localtime(sunSet))     
      print(sunSet)
      sunRise = "Sunrise "+sunRise
      sunSet = "Sunset "+sunSet
   except:
      sunRise= "No sunrise data"
      sunSet= "No sunset data"
   print(sunRise)
   print(sunSet)
   print()
   f.write(sunRise+'\n')
   f.write(sunSet+'\n')
   return
#
# Open a txt file and write data to it sequentially, line by line, to be assembled into a tweet in another script
#
if _platform == "linux" or _platform == "linux2":
   f = open('/home/dougdroplet2/projects/BikeWxX/BikeWxX/data/forecast.txt','w')
   f.write(ymd.strftime("%c")+'\n')
elif _platform == "darwin":
   f = open('data/forecast.txt','w')
   f.write(ymd.strftime("%c")+'\n')
elif _platform == "win32":
   print('if on win32, create a dir and continue')
#
# Call the APIs
#
#
# Basic weather from NWS
#
for city, lat, longit in zip(cities, lats, longits):
   print()
   print(city,lat,longit)
   get_wx(url_wx, lat, longit)
print()
#
# AQI from AirNow
#
for city, lat, longit in zip(cities, lats, longits):
   print()
   print(city,lat,longit,ymd)
   get_aqi(url_aqi, lat, longit, ymd)
print()
#
# Twilight from OpenWeather
#
for city, lat, longit in zip(cities, lats, longits):
   print()
   print(city,lat,longit)
   get_light(url_light, lat, longit)
print()
#
f.close()
