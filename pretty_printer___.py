import requests
import pprint

p=pprint.PrettyPrinter(indent=4)
print(type(p))

result=requests.get("https://open.er-api.com/v6/latest/USD")
data=result.json()

p.pprint(data)