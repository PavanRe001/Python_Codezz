import time
import requests
import datetime
import smtplib
MY_LAT=12.974405
MY_LONG=77.552394

response = requests. get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response. json()

longitude = float(data["iss_position"]["longitude"])
latitude = float(data["iss_position"]["latitude"])
iss_position = (longitude, latitude)
time_now = datetime.datetime.now()

def if_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0
    }
    response = requests.get ("https://api.sunrise-sunset.org/json",params=parameters)
    response.raise_for_status()
    geo_data = response.json()
    sunrise = int(geo_data["results"]["sunrise"].split("T") [1].split(":")[0])
    sunset = int(geo_data["results"]["sunset"].split("T") [1].split(":")[0])
    if sunset <= time_now.hour <= sunrise:
        return True
    else:
        return False

def check_iss_over_head():
    if MY_LAT+5<= latitude<= MY_LAT-5  and MY_LONG+5<= longitude<= MY_LONG+5 :
            return True
    else:
        return False

while True:
    time.sleep(60)
    if check_iss_over_head() and if_night():
        connection= smtplib.SMTP('smtp.gmail.com', 587)
        connection.starttls()
        connection.login('example@gmail.com', 'whbxkazjdgdkutxx')
        connection.sendmail('example@gmail.com', 'sender@gmail.com',
                            "ISS IS OVER YOUR HEAD \n\n ISS will be passing over this hour over your head, "
                            "if you are lucky enough, then you'll get to see the ISS")

