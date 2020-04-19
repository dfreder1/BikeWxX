## Project

Source code for creating a simple twice-daily twitter bot to report the bike commute weather for Sacramento, San Francisco, Silicon Valley, and Portland.

Currently running on twitter bots: @bikewxsac, @BikeWxSF, @BikeWxPDX, and @BikeWxSV

## Operation

'get_wx_data.py' grabs basic weather data from:

https://api.weather.gov/points/

http://www.airnowapi.org/

http://api.openweathermap.org/

https://tidesandcurrents.noaa.gov/api-helper/url-generator.html

and places the data into a text file.

'tweet_wx_data' composes the tweets using the twitter api.


