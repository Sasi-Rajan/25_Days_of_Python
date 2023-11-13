import requests
from datetime import datetime
import smtplib
import time
MY_EMAIL = "sasi.pydev@gmail.com"
MY_PASSWORD = "ukie meud xcgr syvx"
MY_LAT = 10.382900
MY_LNG = 78.815498

        
def iss_overhead():
    try:
        iss_response = requests.get(url="http://api.open-notify.org/iss-now.json")
        iss_response.raise_for_status()
        iss_data = iss_response.json()
    
        iss_latitude = float(iss_data["iss_position"]["latitude"])
        iss_longitude = float(iss_data["iss_position"]["longitude"])
        if (iss_latitude <= MY_LAT+5 and iss_latitude >=MY_LAT-5) and (iss_longitude <=MY_LNG+5 and iss_longitude >=MY_LNG-5):
            return True

    except requests.exceptions.RequestException as e:
        print(f"Error during API request: {e}")
        return False
        
def is_night():  
    try:  
        parameters = {
        "lat": MY_LAT,
        "lng": MY_LNG,
        "formatted": 0
        }
        light_response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
        light_response.raise_for_status()
        data = light_response.json()
        sun_rise = data["results"]["sunrise"].split("T")[1].split(":")[0]
        sun_set = data["results"]["sunset"].split("T")[1].split(":")[0]
        time_now = datetime.now().hour
        if time_now >= sun_set or time_now <=sun_rise:
            return True
        
    except requests.exceptions.RequestException as e:
        print(f"Error during API request: {e}")
        return False

while True: 
    if iss_overhead() and is_night():
        connection=smtplib.SMTP("smtp.gmail.com",port=587)
        connection.starttls()
        connection.login(user=MY_EMAIL,password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg="Subject:ISS Overhead Notifier\n\nHey go and look up on the sky to find me out[ISS]"
        )
        connection.close()
    time.sleep(60)


    
    
    
    
    
    
    