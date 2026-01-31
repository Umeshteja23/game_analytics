import requests
import json

import os
API_KEY = os.getenv("SPORTRADAR_API_KEY")


url = f"https://api.sportradar.com/tennis/trial/v3/en/rankings/doubles.json?api_key={API_KEY}"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    with open("rankings.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)
    print("✅ rankings.json saved successfully")
else:
    print("❌ API failed:", response.status_code, response.text)

