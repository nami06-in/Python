import os
import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

load_dotenv()

class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self._user = os.environ["SHEETY_USRERNAME"]
        self._password = os.environ["SHEETY_PASSWORD"]
        self.sheety_prices_endpoint = os.environ["SHEETY_PRICES_ENDPOINT"]
        self.sheety_users_endpoint = os.environ["SHEETY_USERS_ENDPOINT"]
        self._authorization = HTTPBasicAuth(self._user, self._password)
        self.destination_data = {}
        self.customer_data = {}

    def get_destination_data(self):
        response = requests.get(url=self.sheety_prices_endpoint, auth=self._authorization)
        print(response.text)
        data = response.json()
        print(data)
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                'price': {
                    "iataCode": city["iataCode"]
                }
            }

            response = requests.put(
                url=f"{self.sheety_prices_endpoint}/{city['id']}",
                json=new_data,
                auth=self._authorization)

    def get_customer_emails(self):
        response = requests.get(url=self.sheety_users_endpoint, auth=self._authorization)
        print(response.text)
        data = response.json()
        self.customer_data = data['users']
        return self.customer_data
