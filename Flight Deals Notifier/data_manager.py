import os

import requests
from dotenv import load_dotenv

load_dotenv()

class DataManager:
    def __init__(self):
        self.destination_data = {}
        self.sheety_endpoint = os.getenv('Sheety_Url')
    
    def get_destination_data(self):
        """Fetch all destination data from Sheety"""
        response = requests.get(url=self.sheety_endpoint)
        response.raise_for_status()
        data = response.json()
        self.destination_data = data['prices']
        return self.destination_data
    
    def update_destination_codes(self):
        """Update the IATA codes in the Sheety spreadsheet"""
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{self.sheety_endpoint}/{city['id']}",
                json=new_data
            )
            print(response.text)
