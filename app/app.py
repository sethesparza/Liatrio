import requests 
import json 

api_response = requests.get('app\data.json')
print(api_response.status_code)
data = api_response.text
parse_json = json.loads(data)

print("Todos:", parse_json)

