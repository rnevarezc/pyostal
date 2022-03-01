from requests import Response
from .exceptions import InvalidRequestException

class Response:
    """
    A simple class to handle the Postal API server response:

    This is a very simple translation to Python from my Original PHP Project
    located at https://github.com/rnevarezc/postal
     
    Attributes:
    
        status: The status attribute will give you can indication about whether the
                request  was performed successfully or whether an error occurred.
                Values which may be returned are shown below:
        
                success - this means that the request completed successfully and
                returned what was expected.
                
                parameter-error - the parameters provided for the action are not valid 
                and should be revised.
                
                error - an error occurred that didn't fit into the above categories. 
                This will be accompanied with an error code, a descriptive message and
                further attributes which may be useful. 

        data:   The data attribute contains the result of your request. 
                Depending on the status, this will either contain the data
                requested or details of any error which has occurred.
    """

    status = str

    data = {}

    def __init__(self, response: Response) -> None:
        payload = response.json()
        self.assert_payload(payload)
        self.fill(payload)

    def assert_payload(self, payload): 
        status = payload['status']

        # Postal API is not RESTful, so every request is responded with a 200 code
        # We need to confirm if it is marked as an error.
        if status == 'error' or status == 'parameter-error':
            message = "%s: %s" % (payload['data']['code'], payload['data']['message'])
            raise InvalidRequestException(message)
        return

    def fill(self, payload):
        self.status = payload['status']
        self.time = payload['time']
        self.flags = payload['flags']
        self.data = payload['data']
        return