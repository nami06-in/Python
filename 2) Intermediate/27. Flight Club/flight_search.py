import os
import requests
from dotenv import load_dotenv

load_dotenv()

IATA_ENDPOINT = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
TOKEN_ENDPOINT = "https://test.api.amadeus.com/v1/security/oauth2/token"
FLIGHT_ENDPOINT = "https://test.api.amadeus.com/v2/shopping/flight-offers"


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self._api_key = os.environ["AMADEUS_API_KEY"]
        self._api_secret = os.environ["AMADEUS_API_SECRET"]
        self._token = self._get_new_token()

    def _get_new_token(self):
        header = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        body = {
            'grant_type': 'client_credentials',
            'client_id': self._api_key,
            'client_secret': self._api_secret
        }
        response = requests.post(url=TOKEN_ENDPOINT, headers=header, data=body)
        return response.json()["access_token"]

    def get_destination_code(self, city_name):
        header = {"Authorization": f"Bearer {self._token}"}
        query = {
            "keyword": city_name,
            "max": 2,
            "include": "AIRPORTS",
        }

        response = requests.get(url=IATA_ENDPOINT, headers=header, params=query)
        try:
            code = response.json()["data"][0]['iataCode']
        except KeyError:
            return "Not Found"
        return code

    def check_flights(self, origin_city_iata, destination_iata, from_time, to_time, is_direct=True):
        header = {"Authorization": f"Bearer {self._token}"}
        query = {
            "originLocationCode": origin_city_iata,
            "destinationLocationCode": destination_iata,
            "departureDate": from_time.strftime("%Y-%m-%d"),
            "returnDate": to_time.strftime("%Y-%m-%d"),
            "adults": 1,
            "nonStop": "true" if is_direct else "false",
            "currencyCode": "GBP",
            "max": 10
        }

        response = requests.get(url=FLIGHT_ENDPOINT, headers=header, params=query)

        if response.status_code != 200:
            print(response.status_code)
            print("There was a problem with flight search!")
            print(response.text)
            return None

        return response.json()
