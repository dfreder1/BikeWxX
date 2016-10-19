import tweepy
from sys import platform as _platform
#
# Below required until server upgrade to 2.7.10
import logging
logging.captureWarnings(True)
#
station_id = ['sac','SF','PDX','SV']
#
dict={}
#
for x in range(0,len(station_id)):
    if _platform == "linux" or _platform == "linux2":
        f = open('/home/dougdroplet2/projects/BikeWxX/BikeWxX/keys/'+station_id[x]+'keys','r')
    #    e = open('/var/www/html/bikewxx/data/'+station_id[x]+'amforecast.txt','r')
    elif _platform == "darwin":
        f = open('keys/'+station_id[x]+'keys','r') 
    #    e = open('data/'+station_id[x]+'amforecast.txt','r')
    elif _platform == "win32":
        print 'not supported'
    dict = eval(f.read())
    auth = tweepy.OAuthHandler(dict['API_KEY'], dict['API_SECRET'])
    auth.set_access_token(dict['ACCESS_TOKEN'], dict['ACCESS_TOKEN_SECRET'])
    api = tweepy.API(auth)
    tweetext = e.readline()+e.readline()+e.readline()
    #tweetext = 'test'
    print tweetext
#
    api.update_status(tweetext) 
#
    print 'tweets away!'
