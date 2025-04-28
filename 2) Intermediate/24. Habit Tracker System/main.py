"""
    Reffer https://pixe.la/
    graph id -> It has to start off with some letters from A to Z, and then it could be letters or numbers. 
                And it has to be between 1 and 16 characters. Validation rule: ^[a-z][a-z0-9-]{1,16}
                
"""

import requests
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()

USERNAME = os.getenv("PIXELA_USERNAME")
TOKEN = os.getenv("PIXELA_TOKEN")
GRAPH_ID = "graph1"


'''
   Create Account:-
'''
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    'token': TOKEN, # if facing error put token directly here
    'username': USERNAME, # if facing error, put username directly here.
    'agreeTermsOfService': "yes",
    'notMinor': "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)


'''
   Create Graph:-
'''
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    'id': GRAPH_ID,
    'name': "Cycling Graph",
    'unit': "Km",
    'type': "float",
    'color': "momiji"
}

headers = {
    'X-USER-TOKEN': TOKEN,
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)


'''
   Create Pixel Now:-
'''
pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

now = datetime.now()

pixel_data = {
    'date': now.strftime("%Y%m%d"),
    'quantity': input("How many Kilometers did you cycle today? ")
}

# response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
# print(response.text)


'''
    Update Pixel:-
'''
update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{now.strftime('%Y%m%d')}"

pixel_update_data = {
    'quantity': "4.5",
}

# response = requests.put(url=update_endpoint, json=pixel_update_data, headers=headers)
# print(response.text)


'''
   Delete Pixel:-
'''
delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{now.strftime('%Y%m%d')}"

# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)
