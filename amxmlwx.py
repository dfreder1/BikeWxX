import socket
from sys import platform as _platform
import urllib2
from lxml import etree
import requests
#
# amxmlwx.py
#
print 'running lxml with etree...' 
station_id = ['sac','SF','PDX','SV']
lat = ['38.52','37.77', '45.52','37.39']
longit = ['-121.47','-122.38','-122.67','-122.08']
timeout = 2200
socket.setdefaulttimeout(timeout)
#
for x in range(0,len(station_id)):
    print('Getting station '+station_id[x]+'...')
    print 'Getting first url...'
    url = 'http://graphical.weather.gov/xml/SOAP_server/ndfdXMLclient.php?whichClient=NDFDgen&lat='+lat[x]+'&lon='+longit[x]+'&requestedTime=&startTime=&endTime=&compType=&propertyName=&product=time-series&begin=&end=&Unit=e&temp=temp&wspd=wspd&wdir=wdir&wx=wx&wwa=wwa&Submit=Submit'
    tree = etree.parse(url)
#
#  Get the date from the file 
    todayDate = tree.xpath("//time-layout/start-valid-time/text()")[0]
    print todayDate
#
#  This is run in the morning, get Morning Afternoon Temperatures
    pmT = tree.xpath("//temperature[@type='hourly']/value/text()")[3]
    print pmT
    amT = tree.xpath("//temperature[@type='hourly']/value/text()")[0]
    print amT
#
#  Wind Speed 
    print tree.xpath("//wind-speed/name/text()")[0]
    pmWndSpd = tree.xpath("//wind-speed/value/text()")[3]
    print pmWndSpd+' knots'
    pmWndSpd = str(int(float(pmWndSpd)*1.15))
    print pmWndSpd+' mph'
    amWndSpd = tree.xpath("//wind-speed/value/text()")[0]
    print amWndSpd+' knots'
    amWndSpd = str(int(float(amWndSpd)*1.15))
    print amWndSpd+' mph'
#
#  Wind Direction 
    print tree.xpath("//direction/name/text()")[0]
    pmWndDir = tree.xpath("//direction/value/text()")[3]
    print pmWndDir
    amWndDir = tree.xpath("//direction/value/text()")[0]
    print amWndDir
#
# Go to another url for weather and rain chance
#
    print 'Getting second url for weather summary and rain chance...'
    url = 'http://graphical.weather.gov/xml/SOAP_server/ndfdSOAPclientByDay.php?whichClient=NDFDgenByDay&lat='+lat[x]+'&lon='+longit[x]+'&listLatLon=&lat1=&lon1=&lat2=&lon2=&resolutionSub=&endPoint1Lat=&endPoint1Lon=&endPoint2Lat=&endPoint2Lon=&zipCodeList=&centerPointLat=&centerPointLon=&distanceLat=&distanceLon=&resolutionSquare=&citiesLevel=&format=12+hourly&numDays=1&Unit=e&Submit=Submit'
    tree = etree.parse(url)
#
#  Basic Weather Description 
    basicwx= tree.xpath("//@weather-summary")[0]
    print basicwx
#
#  Probability of Precipitation
    print tree.xpath("//probability-of-precipitation/name/text()")[0]
    pmPofP = tree.xpath("//probability-of-precipitation/value/text()")[1]
    print pmPofP
    amPofP = tree.xpath("//probability-of-precipitation/value/text()")[0]
    print amPofP
#
    amWndDirI = int(amWndDir)
    amWndDirT = 'N'
    if amWndDirI < 315:
        amWndDirT = 'W'
    if amWndDirI < 225:
        amWndDirT = 'S'
    if amWndDirI < 135:
        amWndDirT = 'E'
    if amWndDirI < 45:
        amWndDir = 'N'
    print amWndDirT
#    
    pmWndDirI = int(pmWndDir)
    pmWndDirT = 'N'
    if pmWndDirI < 315:
        pmWndDirT = 'W'
    if pmWndDirI < 225:
        pmWndDirT = 'S'
    if pmWndDirI < 135:
        pmWndDirT = 'E'
    if pmWndDirI < 45:
        pmWndDir = 'N'
    print pmWndDirT
#
#  put the tweet together
    tweetext = basicwx+' Today.\n'+'Ride in: '+amT+'F, wind '+amWndSpd+' from '+amWndDirT+', chance of rain '+amPofP+'%.\n'+'Ride home: '+pmT+'F, wind '+pmWndSpd+' from '+pmWndDirT+', chance of rain '+pmPofP+'%.'
#
    if _platform == "linux" or _platform == "linux2":
        f = open('/home/dougdroplet2/projects/BikeWxX/BikeWxX/data/'+station_id[x]+'forecast.txt','w')
        f.write(tweetext)
    elif _platform == "darwin":
        f = open('data/'+station_id[x]+'forecast.txt','w')
        f.write(tweetext)
#    f.write('\n'+str(todayDate)+' '+tweetext)
    f.close()
#
#
#  Now can form the tweet from another script
