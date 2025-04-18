import json
import pandas as pd
import requests

url = "https://indian-stock-exchange-api2.p.rapidapi.com/corporate_actions"

querystring = {"stock_name":"infosys"}

headers = {
	"x-rapidapi-key": "408e1b2b52msh98ec5eb954da18fp176175jsnde8996a1d5bf",
	"x-rapidapi-host": "indian-stock-exchange-api2.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())

data = response.json()
actions = data.get("corporate_actions", [])
df = pd.DataFrame(actions)

with open("actions_infosys.json", "w") as json_file:
    json.dump(data, json_file, indent=4)  