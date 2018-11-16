import hashlib
from sys import platform as _platform
#
#
station_id = ['sac','SF','PDX','SV']
#
dict={}
#
# Get the forecast txt and hash it
#
for x in range(0,len(station_id)):
    if _platform == "linux" or _platform == "linux2":
        e = open('/home/dougdroplet2/projects/BikeWxX/BikeWxX/data/'+station_id[x]+'forecast.txt','r')
    elif _platform == "darwin":
        e = open('data/'+station_id[x]+'forecast.txt','r')
    elif _platform == "win32":
        print 'not supported'
    #dict = eval(f.read())
# Can't hash a file or place a method within the function (which seems odd)    
    tweetext = e.readline()+e.readline()+e.readline()
    sha1Hash = hashlib.sha1(tweetext)
    sha1HashHexDigest = sha1Hash.hexdigest()
    #
    print "File Name: %s" % e 
#    print "MD5: %r" % md5Hashed
    print "SHA1: %r" % sha1Hash
    print "SHA1: %r" % sha1HashHexDigest
    print tweetext
    e.close()
#
# Write the hash to file for later comparison
#
    if _platform == "linux" or _platform == "linux2":
        g = open('/home/dougdroplet2/projects/BikeWxX/BikeWxX/data/lasthash/'+station_id[x]+'hash','w')
    elif _platform == "darwin":
        g = open('data/'+station_id[x]+'hash','w') 
    elif _platform == "win32":
        print 'not supported'
    g.write(sha1HashHexDigest)
    g.close()
#
# Compare new with old (this will always compare as true in this test script!)

# Change the below to read 'badsachash' as a test

#
    if _platform == "linux" or _platform == "linux2":
        g = open('/home/dougdroplet2/projects/BikeWxX/BikeWxX/data/lasthash/'+station_id[x]+'hash','r')
    elif _platform == "darwin":
        g = open('data/'+station_id[x]+'hash','r') 
    elif _platform == "win32":
        print 'not supported'
#
    yesterdaysHashHexDigest = g.readline()
    if sha1HashHexDigest == yesterdaysHashHexDigest: 
        print 'Hashes match, dont tweet out because it is same as yesterday'
    else:
        print 'Hashes dont match, so go ahead and tweet out because it is not same as yesterday'
#
    g.close()
