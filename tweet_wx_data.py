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
#   If it is before noon, send the ridein, so i=0
#   If it is after noon, send the ridehome, so i=1
#
now = datetime.datetime.now()
i=0
#   
for city in cities:
    if _platform == "linux" or _platform == "linux2":
        e = open('/home/dougdroplet2/projects/BikeWxX/BikeWxX/keys/'+city+'keys','r')
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
        ride='Ride in:\n'
        tweetext = ride+tweettextlist[i+1]+tweettextlist[i+9]+tweettextlist[i+17]  
        tweetext = tweetext + 'Ride home:' + '\n' + tweettextlist[i+1]
    else:
        ride='Ride home:\n'
        tweetext = ride+tweettextlist[i+1]+tweettextlist[i+10]+tweettextlist[i+18]  
    print(tweetext)
    api.update_status(tweetext) 
    print()
    print('tweets away!')
    i += 2
    e.close
#
