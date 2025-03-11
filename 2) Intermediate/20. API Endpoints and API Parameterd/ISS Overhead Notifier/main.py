"""
   Copy the ISS Enpoint API from this -> https://open-notify.org/Open-Notify-API/ISS-Location-Now/
   and paste it on a new tab. You will see a JSON format of current address of the ISS.
   If you refresh the page the data will be slightly different since the ISS is moving.

   To get latitude and longitude of a place: https://www.latlong.net/
   Use your own email and password as discussed in 'birthday wisher' project.

   To see the code works, use the current Latitude and Longitude of ISS.
"""

import requests
import pytz
from datetime import datetime
from dotenv import load_dotenv
import os
import smtplib
import time

load_dotenv()
MY_EMAIL = os.getenv("EMAIL")
MY_PASSWORD = os.getenv("EMAIL_PASSWORD")

MY_LAT = os.getenv("MY_LAT")  # Your latitude
MY_LONG = os.getenv("MY_LONG")  # Your longitude


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # Your position is within +5 or -5 degrees of the ISS position.
    if (MY_LAT - 5 <= iss_latitude <= MY_LAT + 5) and (MY_LONG - 5 <= iss_longitude <= MY_LONG + 5):
        return True


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = data["results"]["sunrise"]
    sunset = data["results"]["sunset"]

    fmt = "%Y-%m-%dT%H:%M:%S%z"
    utc_sunrise_dt = datetime.strptime(sunrise, fmt)
    utc_sunset_dt = datetime.strptime(sunset, fmt)

    # Convert to local timezone (replace 'Asia/Kolkata' with your timezone)
    local_timezone = pytz.timezone("Asia/Kolkata")
    local_sunrise = utc_sunrise_dt.astimezone(local_timezone)
    local_sunset = utc_sunset_dt.astimezone(local_timezone)

    # Extract hour for sunrise and sunset
    sunrise_hour = int(local_sunrise.hour)
    sunset_hour = int(local_sunset.hour)

    time_now = datetime.now().hour
    if time_now >= sunset_hour or time_now <= sunrise_hour:
        return True


while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg="Subject:Look Up☝️!\n\nThe ISS is above you in the sky."
            )


# If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
