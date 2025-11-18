import requests

url = "https://jsearch.p.rapidapi.com/search"

params = {
    "query":
    "developer jobs in chicago",
    "page":"1",
    "num_pages":"1",
    "country":"us",
    "date_posted":"all"
}

headers = {
	"x-rapidapi-key": "key",
	"x-rapidapi-host": "jsearch.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=params)

print(response.json())