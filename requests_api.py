import json
import requests

api_url = "https://api.api-ninjas.com/v1/dogs"
xApiKey = "sQxDQkf25FN9EPc9Xm+dsA==SDLtnGbXN2Rxeiz8"

def fetchDogs(breed):
    url = api_url + "?name={}".format(breed)

    response = requests.get(url, headers={'X-Api-Key': xApiKey})

    if response.status_code == requests.codes.ok:
        return response.text
    else:
        print("Error:", response.status_code, response.text)
        
dog = json.loads(fetchDogs("golden"))[0]

print(dog)