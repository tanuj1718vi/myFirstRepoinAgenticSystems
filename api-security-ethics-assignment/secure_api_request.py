import os
import requests

# Get API key
api_key = os.getenv("API_KEY")

if not api_key:
    print("API key not found. Please set the environment variable.")
    exit()

url = "https://api.example.com/data"

headers = {
    "Authorization": f"Bearer {api_key}"
}

try:
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        print("Success:")
        print(response.json())

    elif response.status_code == 429:
        print("Rate limit reached. Try again later.")

    else:
        print("Request failed. Status code:", response.status_code)

except requests.exceptions.RequestException as e:
    print("Error occurred while making request:")
    print(e)