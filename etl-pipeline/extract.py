import requests
import os
import json
from datetime import datetime as dt
from dotenv import load_dotenv

load_dotenv()  # loads api key from .env file
API_KEY = os.getenv("API_KEY")

#API endpoint and parameters
url = "https://jsearch.p.rapidapi.com/search"

params = {
    "query":"software developer",
    "page":"1",
    "country": "australia",
    "num_pages":"2",
    "date_posted":"week"
}

headers = {
	"x-rapidapi-key": API_KEY,
	"x-rapidapi-host": "jsearch.p.rapidapi.com"
}

def extract_jobs():
    os.makedirs('rawData', exist_ok=True)
    print("Extracting job data...")
    response = requests.get(url, headers=headers, params=params)

    if response.status_code != 200:
        raise Exception(f"API request failed with status code {response.status_code}")
    
    data = response.json()

    # keeping track of raw data
    timestamp = dt.now().strftime("%Y%m%d_%H%M%S")
    raw_filename = f"rawData/jobs_raw_{timestamp}.json"

    with open(raw_filename, 'w') as f:
        json.dump(data, f, indent=4)
    print(f"Saved raw data → {raw_filename}")
    return raw_filename