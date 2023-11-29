import requests as req
from datetime import datetime
USERNAME="sasi"
PASSWORD="qwerty12345"
API_ID="38d7a7e0"
API_KEY="f72c8ca37bfa847c9c248e66c8284c59"
GENDER="male"
WEIGHT_KG=72
HEIGHT_CM=175
AGE=21
sheet_endpoint = "https://api.sheety.co/13f245e0b0d27892919fbe78d7e89014/workoutTracking/workouts"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": API_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json"
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response=req.post(url=exercise_endpoint,headers=headers,json=parameters)
output=response.json()


today_date = datetime.now().strftime(r"%d/%m/%Y")
now_time = datetime.now().strftime(r"%X")

for exercise in output["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    sheet_response = req.post(sheet_endpoint, json=sheet_inputs, auth=(USERNAME,PASSWORD))

    print(sheet_response.text)