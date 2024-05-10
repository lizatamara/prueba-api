import requests
import json

def request_get(url):
    return json.loads(requests.get(url).text)