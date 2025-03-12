"""
      Call 5 day / 3 hour forecast data: https://openweathermap.org/forecast5
   1. Get your latitude and longitude from latlong.net
   2. Make a request to the forecast API using the requests module.
   3. Print out the http status code that you get back.
   4. Print the response to the console.
   5. Copy-paste the response to an online JSON viewer: https://jsonviewer.stack.hu/
   6. Locate the weather id and description for each forecast.

   cnt parameter: By setting the count to four, we'll request only four timestamps covering the 
                  12-hour window that matters to us.

   weather condition codes: https://openweathermap.org/weather-conditions#Weather-Condition-Codes-2
   These codes can be seen in the 'id'
   if the weather id is less than 700 then you should bring umbrella.

   CHALLENGE: Objective-
              Print "Bring an Umbrella" if any of the weather condition codes is less than 700 in the next 12-hour window.
              HINTS-
              1. First, see if you can print out he weather id in thw first forecast.
              2. Then try and create a list of the condition codes spanning the next 12 hours.

    Register a twilio account -> https://www.twilio.com/en-us

"""

import requests
from twilio.rest import Client
from dotenv import load_dotenv
import os

load_dotenv()

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = os.getenv("RAIN_ALERT_API_KEY")
account_sid = os.getenv("TWILIO_SID")
auth_token = os.getenv("TWILIO_TOKEN")
MY_LAT = os.getenv("MY_LAT")
MY_LONG = os.getenv("MY_LONG") 

weather_params = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": api_key,
    "cnt": 4,
}
response = requests.get(url=OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data['weather'][0]['id']
    condition_description = (hour_data['weather'][0]['description']).title()
    if int(condition_code) < 600:
        will_rain = True
        break

code_str = str(condition_code)
if code_str[0] == '5':
    emoji = '🌧️'
elif code_str[0] == '3':
    emoji = '🌦️'
elif code_str[0] == '2':
    emoji = '⛈️'
else:
    emoji = '☁️'

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_=f'whatsapp:{os.getenv("TWILIO_NUMBER")}',
        body=f'Weather Now: "{condition_description}" {emoji}\nIt\'s going to rain today. '
             f'Remember to carry an Umbrella ☔',
        to=f'whatsapp:{os.getenv("MY_WHATSAPP_NUMBER")}'
    )
    print(message.status)
