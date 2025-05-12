import requests
from datetime import datetime
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv
import os

load_dotenv()

APP_ID = os.getenv("NUTRITION_APP_ID")
API_KEY = os.getenv("NUTRITION_API_KEY")
NLEndpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
Sheety_Endpoint = "https://api.sheety.co/6bc90a36aa3a460605da474d24721ac0/workoutTracking/workouts"

NL_parameters = {
    'query': input("Tell me which exercises you did: "),
}

headers = {
    'x-app-id': APP_ID,
    'x-app-key': API_KEY,
}

NL_response = requests.post(url=NLEndpoint, json=NL_parameters, headers=headers)
NL_data = NL_response.json()['exercises']

now = datetime.now()
header1 = {
    "Authorization": os.getenv("SHEETY_AUTHORIZATION_1")
}

header2 = {
    "Authorization": os.getenv("SHEETY_AUTHORIZATION_2")
}

for exercise in NL_data:
    sheety_parameters = {
        "workout": {
            'date': now.strftime("%d/%m/%Y"),
            'time': now.strftime("%X"),
            'exercise': exercise['name'].title(),
            'duration': exercise['duration_min'],
            'calories': exercise['nf_calories'],
        }
    }

    sheety_response = requests.post(url=Sheety_Endpoint, json=sheety_parameters, headers=header2)
    print(sheety_response.text)
