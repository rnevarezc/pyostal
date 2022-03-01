import requests
from .response import Response

class Client:
    """ 
    A simple Client class to use the Postal Server API

    This is a very simple translation to Python from my Original PHP Project
    located at https://github.com/rnevarezc/postal

    It uses the great psf/requests library to handle all the http weight-lifting.
    
    Attributes:
        host:       The Postal Host that will be used.
        apikey:     The provided apikey
        headers:    Any additional headers to be passed to the api.
    """

    def __init__(self, host: str, apikey: str, headers = {}) -> None:
        self.host = host
        self.apikey = apikey
        self.headers = headers

    def get_headers(self) -> dict:
        default_headers = {
            'X-Server-API-Key': self.apikey,
            'content-type': 'application/json'
        }
        return self.headers | default_headers

    def __get_postal_uri(self, resource: str, action: str) -> str:
        return "%s/api/v1/%s/%s" % (self.host, resource, action)

    def __perform_request(
        self, resource: str, action: str, payload: dict
    ) -> Response:
        return requests.post(
            self.__get_postal_uri(resource, action),
            json = payload,
            headers = self.get_headers()
        )
        
    async def send(self, payload: dict):
        response = self.__perform_request('send', 'message', payload)
        return Response(response)