import os
import requests
import time
from dotenv import load_dotenv 


load_dotenv()

api_key = os.environ.get("API_KEY")

city = "Hyderabad"

url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

# Handling
try:
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print("Weather fetched successfully!")

    elif response.status_code == 429:
        print("Too many requests. Please try again later.")
        time.sleep(4)

    else:
        print(f"Error: {response.status_code}")

except Exception as e:
    print("Something went wrong:", e)







