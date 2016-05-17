from sys import platform as _platform
import tweepy
#
station_id = ['MSP']
#
#
dict={}
if _platform == "linux" or _platform == "linux2":
    e = open('/var/www/html/bikewxx/data/'+station_id[0]+'amforecast.txt','r')
    f = open('/var/www/html/bikewxx/keys/MSPkeys','r')
    dict = eval(f.read())
elif _platform == "darwin":
    e = open('data/'+station_id[0]+'amforecast.txt','r')
    f = open('keys/MSPkeys','r') 
    dict = eval(f.read())
elif _platform == "win32":
    print 'not supported'
print dict
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
