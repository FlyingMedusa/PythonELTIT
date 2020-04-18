import requests
import json


def piratetrans(text):
    url = 'https://api.funtranslations.com/translate/pirate.json'
    data = {'text': text}

    response = requests.post(url, data=data)
    json_data = json.loads(response.text)
    print(json_data['contents']['translated'])


piratetrans('Hello sir')