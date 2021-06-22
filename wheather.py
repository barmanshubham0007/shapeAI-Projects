import requests
import logging

from datetime import datetime

api_key = '87d845b0b6cf29baa1a73cc34b067a95'
location = input("Enter city name: ")

link_api = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(link_api)
api_data = api_link.json()

temp = ((api_data['main']['temp']) - 273.15)
weatherDesc = api_data['weather'][0]['description']
humidity = api_data['main']['humidity']
windSpeed = api_data['wind']['speed']
dateTime = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

print ("_________________________________________________________________")
print ("Weather Stats for - {}  || {}".format(location.upper(), dateTime))
print ("_________________________________________________________________")

print ("Current temperature is: {:.2f} deg C".format(temp))
print ("Current weather desc  :",weatherDesc)
print ("Current Humidity      :",humidity, '%')
print ("Current wind speed    :",windSpeed,' kmph')

# Logging wheather details in a text file.
logging.basicConfig(filename="wheather.log",format='%(asctime)s %(message)s',filemode='a')

logger=logging.getLogger()

logger.setLevel(logging.DEBUG)

logger.info("Weather Stats for - {}  || {}: ".format(location.upper(), dateTime))

logger.info("Current temperature is: {:.2f} deg C".format(temp))
logger.info("Current weather desc  : {}".format(weatherDesc))
logger.info("Current Humidity      : {} %".format(humidity))
logger.info("Current wind speed    : {} kmph \n".format(windSpeed))