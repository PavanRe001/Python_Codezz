import requests
import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()
TOKEN_URL = 'https://test.api.amadeus.com/v1/security/oauth2/token'
FLIGHT_ENDPOINT = 'https://test.api.amadeus.com/v2/shopping/flight-offers'

class FlightSearch():
    def __init__(self):
        self.API_ID = os.getenv('Amadeus_API_ID')
        self.API_KEY = os.getenv('Amadeus_API_KEY')
        # self.API_ID = 'dCFyMWLMCxItv32b09AlCI0vck0jXfLG'
        # self.API_KEY = 'C30JhtP9UFAwgWi5'
        self._token = self.get_token()
    
    def get_token(self):
        """Get OAuth token from Amadeus API"""
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        
        data = {
            'grant_type': 'client_credentials',
            'client_id': self.API_ID,
            'client_secret': self.API_KEY
        }
        
        response = requests.post(url=TOKEN_URL, headers=headers, data=data)
        response.raise_for_status()
        fetched_data = response.json()['access_token']
        return fetched_data

    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        """Search for flight offers between two cities"""
        headers = {"Authorization": f"Bearer {self._token}"}
        
        query = {
            "originLocationCode": origin_city_code,
            "destinationLocationCode": destination_city_code,
            "departureDate": from_time.strftime("%Y-%m-%d"),
            "returnDate": to_time.strftime("%Y-%m-%d"),
            "adults": 1,
            "nonStop": "true",
            "currencyCode": "INR",
            "max": "10",
        }

        response = requests.get(
            url=FLIGHT_ENDPOINT,
            headers=headers,
            params=query,
        )

        if response.status_code != 200:
            print(f"check_flights() response code: {response.status_code}")
            print("There was a problem with the flight search.\n"
                  "For details on status codes, check the API documentation:\n"
                  "https://developers.amadeus.com/self-service/category/flights/api-doc/flight-offers-search/api-reference")
            print("Response body:", response.text)
            return None

        return response.json()
