import requests
from datetime import datetime
import os
import os
from dotenv import load_dotenv

load_dotenv()
APP_ID = os.getenv("APP_ID")
API_KEY = os.getenv("API_KEY")
API_ENDPOINT = "https://trackapi.nutritionix.com/V2/natural/exercise"
USER_NAME = os.getenv("USER_NAMED")
SHEETY_TOKEN = os.getenv("SHEETY_TOKEN")

#DATE and TIME
standard_date = datetime.now()
date = standard_date.strftime("%d/%m/%Y")
time = standard_date.strftime("%H:%M:%S")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}
parameters = {
    "query": "I walk around 2 Miles and swim 30 minutes"
}

project_name = "myWorkouts"
sheet_name = "workouts"
sheety_endpoint = "https://api.sheety.co/c2b5d4ec3403081b7f36b55dabb4c9f1/workoutTracker/sheet1"
sheety_headers = {
    "Authorization": SHEETY_TOKEN
}

response = requests.post(url=API_ENDPOINT, json=parameters, headers=headers)
list_of_exercises = response.json()["exercises"]

for exercise in list_of_exercises:
    data = {
        "sheet1": {
            "date": date,
            "time": time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }
    res = requests.post(url=sheety_endpoint, json=data, headers=sheety_headers)
    res.raise_for_status()

