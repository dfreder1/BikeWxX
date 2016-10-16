import tweepy
from sys import platform as _platform
#
station_id = ['MSP']
#
dict={}
if _platform == "linux" or _platform == "linux2":
    e = open('/home/dougdroplet2/projects/BikeWxX/BikeWxX/data/'+station_id[x]+'pmforecast.txt','r')
    f = open('/home/dougdroplet2/projects/BikeWxX/BikeWxX/keys/MSPkeys.txt','r')
    dict = eval(f.read())
elif _platform == "darwin":
    e = open('data/'+station_id[x]+'pmforecast.txt','r')
    f = open('keys/MSPkeys','r') 
    dict = eval(f.read())
elif _platform == "win32":
    print 'not supported'
#
auth = tweepy.OAuthHandler(dict['API_KEY'], dict['API_SECRET'])
auth.set_access_token(dict['ACCESS_TOKEN'], dict['ACCESS_TOKEN_SECRET'])
api = tweepy.API(auth)
#
tweetext = e.readline()+e.readline()+e.readline()
print tweetext
#
api.update_status(tweetext) 
#
print 'tweets away!'
