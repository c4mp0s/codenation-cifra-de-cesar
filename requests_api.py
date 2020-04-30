import requests
import json

class Requests:
    def __init__(self, token):
        self._base_url_get = 'https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token='+token
        self._base_url_post = 'https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token='+token

    def get(self):
        response = requests.get(self._base_url_get).json()
        return response
    
    def post(self):
        files = [('answer', open('answer.json','rb'))]
        response = requests.request("POST", self._base_url_post, files = files)
        response = json.dumps(response.text)
        return response

