import requests
import datetime
APP_ID='app_bec78a9f42dc4834bdd97176'
APP_KEY='nix_live_CzQDjwMpxTDu4BatigItlD3Imb8nOsGp'
WEB_LINK='https://app.100daysofpython.dev/v1/nutrition/natural/exercise'


desc=str(input('Tell me which exercises you did?'))

headers={
    'x-app-id': APP_ID,
    'x-app-key': APP_KEY,
    'Content-Type': 'application/json',
}

parameters={
    "query": desc,
    "weight_kg": 70,
    "height_cm": 175,
    "age": 18,
    "gender": "male"
}

response=requests.post(url=WEB_LINK,headers=headers,json=parameters)
response.raise_for_status()

result=response.json()
print(result)


today=datetime.datetime.now()
datestamp=today.strftime('%d/%m/%Y')
timestamp=today.strftime('%X')

for exercise in result["exercises"]:
    json_data = {
        'workout':{
            'date':datestamp,
            'time':timestamp,
            'exercise':exercise['name'].title(),
            'duration':exercise['duration_min'],
            'calories':exercise['nf_calories']
        }
    }
    sheet_url='https://api.sheety.co/2d81c76f0dcd01568ea249d5287659c0/workoutTracker/workouts'
    sheet_response=requests.post(url=sheet_url,json=json_data)
    print(sheet_response.text)



