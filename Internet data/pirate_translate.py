from googletrans import Translator
import requests


def piratetrans(text):
    url = 'https://api.funtranslations.com/translate/pirate.json'
    data = {'text': text}
    response = requests.post(url, data=data)
    print(response.text)


piratetrans('Hello sir')