# Python 3
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
dat = ymd.strftime("%Y")+ymd.strftime("%m")+ymd.strftime("%d")
#
# Define the 'base' of the four api requests used, will later add on to these strings
#
url_wx = 'https://api.weather.gov/points/'
url_aqi = 'http://www.airnowapi.org/aq/forecast/latLong/?format=application/json&'
url_light = 'http://api.openweathermap.org/data/2.5/weather?'
url_tide = 'https://tidesandcurrents.noaa.gov/api/datagetter?begin_date='+dat+'&range=48&station=9414290&product=predictions&datum=NAVD&time_zone=lst&interval=hilo&units=english&application=bikewxx&format=json'
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
   status = r.status_code
   print(status)
   if status != 200:
      time.sleep(300)
      r = requests.get(url)
      status = r.status_code
      print(status,1)
   if status != 200:
      time.sleep(300)
      r = requests.get(url)
      status = r.status_code
      print(status,2)
   if status != 200:
      print(status,3)
      print('No data after 3 tries') 
   if status == 200:
      json_data = r.json()
#      print(json_data)
#      print("")
#      print(url)
#      print(json_data['properties']['periods'][1])
# 
#  Get the time of "period 1" (which is 0 on the list), then use that info to find which period to grab. For ride in you want 15:00 UTC, and for ride home you want 00:00 UTC.
#  The chron job runs at 4 am which is 11 utc, and at 3 pm which is 23 utc  
#
      startTime = json_data['properties']['periods'][0]['startTime']
      print(startTime)
      startTime = int(startTime[11:13])
      if startTime < 15:
         needPeriod = 1+15-startTime
      else:
         needPeriod = 1+24-startTime
      print(startTime)
      print(needPeriod)
      #
      ridein = json_data['properties']['periods'][needPeriod]['shortForecast'] + ', '\
       +json.dumps(json_data['properties']['periods'][needPeriod]['temperature'])      \
       +json_data['properties']['periods'][needPeriod]['temperatureUnit'] \
       +', Wind '\
       +json_data['properties']['periods'][needPeriod]['windSpeed']        + ' from '\
       +json_data['properties']['periods'][needPeriod]['windDirection']
       #
      needPeriod = needPeriod + 8
#       +(u'\N{DEGREE SIGN}') \
       #
      ridehome = json_data['properties']['periods'][needPeriod]['shortForecast'] + ', '\
       +json.dumps(json_data['properties']['periods'][needPeriod]['temperature'])      \
       +json_data['properties']['periods'][needPeriod]['temperatureUnit'] \
       +', Wind '\
       +json_data['properties']['periods'][needPeriod]['windSpeed']        + ' from '\
       +json_data['properties']['periods'][needPeriod]['windDirection']
#       +(u'\N{DEGREE SIGN}') \
   else:
      print(status)
      ridein = 'No data'
      ridehome = 'No data'
   print(ridein)
   print(ridehome)
   f.write(ridein+'\n')
   f.write(ridehome+'\n')
   return
#
# Function for AQI from AirNow
#
def get_aqi(baseurl,lat,longit,ymd):
   "This function calls the AQI from AirNow"
   # Requires API Key so find it
   if _platform == "linux" or _platform == "linux2":
       e = open('/home/dougdroplet2/projects/BikeWxX/bikewxxkeys/AQIkey','r')
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
      print(status,1)
   if status != 200:
      time.sleep(300)
      r = requests.get(url)
      status = r.status_code
      print(status,2)
   if status != 200:
      print('No data after 3 tries') 
      print(status,3)
   if status == 200:
      print(status)
      json_data = r.json()
      #print(json_data)
      # Always get the 0 data which is the AQI for this day, as there is only 1 forecast per day provided by the API
      rideinAqi = "AQI: "+(json_data[0]['Category']['Name'])
      ridehomeAqi = rideinAqi 
      # with the index number ridehomeAqi = "Air Quality Index "+json.dumps(json_data[0]['AQI'])+"-"+(json_data[0]['Category']['Name'])
      # with the index number rideinAqi = "Air Quality Index "+json.dumps(json_data[0]['AQI'])+"-"+(json_data[0]['Category']['Name'])
   else:
      rideinAqi = 'No data'
      ridehomeAqi = 'No data'
   print(rideinAqi)
   print(ridehomeAqi)
   f.write(rideinAqi+'\n') 
   f.write(ridehomeAqi+'\n') 
   print()
   return
#
# Function for twilight data from OpenWeather
# Define bike twilight as sunset and 24 minutes before sunrise
# 24 minutes is 1440 seconds
#
def get_light(baseurl,lat,longit):
   "This function calls the twilight data from OpenWeather"
   # Requires API Key so find it
   if _platform == "linux" or _platform == "linux2":
       g = open('/home/dougdroplet2/projects/BikeWxX/bikewxxkeys/OWMkey','r')
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
      print(status,1)
   if status != 200:
      time.sleep(300)
      r = requests.get(url)
      status = r.status_code
      print(status,2)
   if status != 200:
      print('No data after 3 tries') 
      print(status,3)
   if status == 200:
      print(status)
      json_data = r.json()
      print(json_data)
      sunRise = json_data['sys']['sunrise']
      sunRise = time.strftime("%I:%M %p", time.localtime(sunRise-1440))
      print(sunRise)
      sunSet = json_data['sys']['sunset']
      sunSet = time.strftime("%I:%M %p", time.localtime(sunSet))     
      print(sunSet)
      sunRise = "Bikelights: Before "+sunRise
      sunSet = "Bikelights: After "+sunSet
   else:
      sunRise= "No data"
      sunSet= "No data"
   print(sunRise)
   print(sunSet)
   print()
   # Note that sunrise sunset is now really my definition of Bike Twilight
   f.write(sunRise+'\n')
   f.write(sunSet+'\n')
   return
#
# Function for tide data from NOAA
#
def get_tide(baseurl, city):
  "This function calls the tide data from NOAA using the CO-OPS API"
  # Warning, kluge ahead!
  # This script assembles lines of text to be tweeted. Each line (now 4 lines) comes from each API call.
  # The tide api call and it's corresponding line of text only apply to San Francisco
  # So the kluge is to only run this tide api call on 'Frisco. The fourth line will always be a blank for other cities,
  # but will be either the tide warning or a blank for 'Frisco.
  if city == 'San Francisco,CA':
    url = baseurl
    r = requests.get(url)
    status = r.status_code
    print(url)
    print(status)
    if status != 200:
      time.sleep(300)
      r = requests.get(url)
      status = r.status_code
      print(status,1)
    if status != 200:
      time.sleep(300)
      r = requests.get(url)
      status = r.status_code
      print(status,2)
    if status != 200:
      print(status,3)
      print('No data after 3 tries') 
    if status == 200:
      json_data = r.json()
      print (json_data['predictions'])
      tidev =  max(float(json_data['predictions'][0]['v']),float(json_data['predictions'][1]['v']),float(json_data['predictions'][2]['v']),float(json_data['predictions'][3]['v']))
      if tidev > 6.40:
          tidein = "Today's high tide of " + str(tidev)[:4] + ' could cause path flooding in low areas, see https://tidesandcurrents.noaa.gov/map/index.shtml?id=9414290'
          tidehome = tidein
      else:
          # Assigning 'no data' here but really if it gets here then there is data, it is just data I don't want tweeted
          tidein = 'No data'
          tidehome = tidein
    else:
      print(status)
      tidein = 'No data'
      tidehome = tidein
  #  f.write(tidein+'\n')
  #  f.write(tidehome+'\n')
  else:
    tidein = 'No data'
    tidehome = tidein
  #
  f.write(tidein+'\n')
  f.write(tidehome+'\n')
  return
#
# End of functions
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
# Call the functions which access the four APIs
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
# Tide from NOAA - this is just for 'frisco
#
for city in cities:
  print()
  get_tide(url_tide,city)
print()
#
f.close()
