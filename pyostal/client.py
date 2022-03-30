import requests
from .response import Response
from .emails import Email
from typing import Union

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

    def __get_headers(self) -> dict:
        default_headers = {
            'X-Server-API-Key': self.apikey,
            'content-type': 'application/json'
        }
        return self.headers | default_headers

    def __get_postal_uri(self, resource: str, action: str) -> str:
        return "%s/api/v1/%s/%s" % (self.host, resource, action)

    def __do_request(self, resource: str, action: str, payload: dict):
        return requests.post(
            self.__get_postal_uri(resource, action),
            json = payload,
            headers = self.__get_headers()
        )
        
    async def send(self, email: Union[Email,dict]) -> Response:

        # If we receive a simple dict, then we create an Email instance.
        # This way we are sure the data is set correctly or an Exception
        # will raise.
        email = email if isinstance(email, Email) else Email(**email)  

        request = self.__do_request('send', 'message', email.as_payload())
        response = Response(**request.json())
        email.set_response(response)

        return response

    async def get_message_details(
        self, id: int, expansions: list = ['status','details']) -> Response:
        request = self.__do_request(
            'messages', 'message', {'id': id, '_expansions': expansions}
        )
        return Response(**request.json())
    
    async def get_message_deliveries(self, id: int) -> Response:
        request = self.__do_request('messages', 'deliveries', {'id': id})
        return Response(**request.json())