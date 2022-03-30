from dataclasses import dataclass, field
from .exceptions import InvalidRequestException

@dataclass
class Response:
    """
    A simple class to handle the Postal API server response:

    This is a very simple translation to Python from my Original PHP Project
    located at https://github.com/rnevarezc/postal
     
    Attributes:
        data:   The data attribute contains the result of your request. 
                Depending on the status, this will either contain the data
                requested or details of any error which has occurred.

        flags:  Additional flags provided by the API
    
        status: The status attribute will give you can indication about whether
                the request was performed successfully or whether an error 
                occurred. Values which may be returned are shown below:
        
                success - this means that the request completed successfully and
                returned what was expected.
                
                parameter-error - the parameters provided for the action are not
                valid  and should be revised.
                
                error - an error occurred that didn't fit into the above categories. 
                This will be accompanied with an error code, a descriptive message
                and further attributes which may be useful. 

        time:   The timestamp of the response

        details:Details provided for some error payloads.
    """
    status: str
    time: float = None
    flags: list = field(default_factory=list)
    data: dict = field(default_factory=dict)
    details: dict = field(default_factory=dict)

    def __post_init__(self):

        # Postal API is not RESTful, so every request is responded 
        # with a 200 code. We need to confirm if it is marked as an error.
        if self.status != 'success':

            # Postal API responses are very inconsistent, so we need to try
            # any kind of message received in the payload, otherwise the 
            # message is simply None.
            message = self.data.get('message') or self.details or None
            raise InvalidRequestException(message)
        return