import requests
from datetime import datetime
import smtplib
import time

# TODO - ISS OVERHEAD
#  If the ISS is close to my current position
#  and it is currently dark
#  Then send me an email to tell me to look up.
#  BONUS: run the code every 60 seconds.

MY_LAT = 51.507351  # Your latitude
MY_LONG = -0.127758  # Your longitude
MY_EMAIL = "gmail.com"
MY_PASSWORD = "password"

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

time_now = datetime.now()
parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "date": f"{time_now.year}-{time_now.month}-{time_now.day}",
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

hour = time_now.hour


while True:
    time.sleep(60)  # sleeping time for every 60 seconds
    if (MY_LAT - 5) <= iss_latitude <= (MY_LAT + 5) and (MY_LONG - 5) <= iss_longitude <= (MY_LONG + 5):
        if hour in range(sunset, 24) or hour in range(0, sunrise):
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=MY_EMAIL, password=MY_PASSWORD)
                connection.sendmail(from_addr=MY_EMAIL,
                                    to_addrs="gmail.com",
                                    msg=f"Subject:ISS overhead !!!\n\n"
                                        f"There is iss orbiting above your location\n"
                                        f"Enjoy!!!!")
