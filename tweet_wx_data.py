# Python 3
import tweepy, datetime
from sys import platform as _platform
#
# Define the cities considered
#
cities = ['SAC','SF','PDX','SV']
#
# Open the txt file previously created and create python List of tweets by cycling through the txt file
#
if _platform == "linux" or _platform == "linux2":
   f = open('/home/dougdroplet2/projects/BikeWxX/BikeWxX/data/forecast.txt','r')
elif _platform == "darwin":
   f = open('data/forecast.txt','r')
elif _platform == "win32":
   print('if on win32, create a dir and continue')
#
tweettextlist = []
for item in f:
    tweettextlist.append(item)
f.close
print(tweettextlist[0])
print()
#
# Cycle through the cities, get the keys, make the tweet, send the tweet
#
dict={}
#
#   If it is before noon, send the ridein
#   If it is after noon, send the ridehome
#   Below assumes the server is on local time
now = datetime.datetime.now()
i = 0
#   
for city in cities:
    if _platform == "linux" or _platform == "linux2":
        e = open('/home/dougdroplet2/projects/BikeWxX/bikewxxkeys/'+city+'keys','r')
    elif _platform == "darwin":
        e = open('../bikewxxkeys/'+city+'keys','r') 
    elif _platform == "win32":
        print('create dir and continue')
    dict = eval(e.read())
    auth = tweepy.OAuthHandler(dict['API_KEY'], dict['API_SECRET'])
    auth.set_access_token(dict['ACCESS_TOKEN'], dict['ACCESS_TOKEN_SECRET'])
    api = tweepy.API(auth)
    #
    if datetime.time(now.hour)<datetime.time(12,0):     
        ride='Morning ride in will be '
        #tweetext = ride+tweettextlist[i+1]+tweettextlist[i+9]+tweettextlist[i+17]+tweettextlist[i+25]
        tweetext = ride
        if tweettextlist[i+1][:7] == 'No data':
            tweetext = tweetext
        else:
            tweetext = tweetext + str.lower(tweettextlist[i+1][:1]) + tweettextlist[i+1][1:]
        if tweettextlist[i+9][:7] == 'No data':
            tweetext = tweetext
        else:
            tweetext = tweetext + tweettextlist[i+9]
        if tweettextlist[i+17][:7] == 'No data':
            tweetext = tweetext
        else:
            tweetext = tweetext + tweettextlist[i+17]
        if tweettextlist[i+25][:7] == 'No data':
            tweetext = tweetext
        else:
            tweetext = tweetext + tweettextlist[i+25]
        if tweettextlist[i+2][:7] == 'No data':
            tweetext = tweetext
        else:    
            tweetext = tweetext + 'Ride home will be' + tweettextlist[i+2][8:]
    else:
        ride='Evening ride home will be '
        #tweetext = ride+tweettextlist[i+1]+tweettextlist[i+10]+tweettextlist[i+18]+tweettextlist[i+26]
        tweetext = ride
        if tweettextlist[i+1][:7] == 'No data':
            tweetext = tweetext
        else:
            tweetext = tweetext + str.lower(tweettextlist[i+1][:1]) + tweettextlist[i+1][1:]
        if tweettextlist[i+10][:7] == 'No data':
            tweetext = tweetext
        else:
            tweetext = tweetext + tweettextlist[i+10]
        if tweettextlist[i+18][:7] == 'No data':
            tweetext = tweetext
        else:
            tweetext = tweetext + tweettextlist[i+18]
        if tweettextlist[i+26][:7] == 'No data':
            tweetext = tweetext
        else:
            tweetext = tweetext + tweettextlist[i+26]
    print("")
    print(city)
    print(tweetext)
    #api.update_status(tweetext) 
    print('tweets away!')
    i += 2
    e.close
#
