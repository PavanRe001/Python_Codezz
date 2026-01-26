import requests

response=requests.get("https://api.open-meteo.com/v1/forecast?latitude=12.974405&longitude=77.552394&hourly=temperature_2m,visibility,rain,weather_code&timezone=auto&forecast_days=1")
web_data=response.json()
# print(web_data)
# print(response.status_code)
data=(web_data['hourly']['weather_code'])
if web_data['hourly']['time'][7:18]:
    for _ in data:
        if _ >1:
             print('Partly cloudy sky')

from twilio.rest import Client
account_sid = 'Use Your own'
auth_token = 'Pass_key'
client = Client(account_sid, auth_token)
message = client.messages.create(
    body="Hi God,",
    from_="+1----------",
    to="+91**********",
)
print(message.status)