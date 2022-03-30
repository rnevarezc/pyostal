class PostalException(RuntimeError):
    pass

class InvalidRequestException(PostalException):
    pass

class InvalidEventPayloadException(PostalException):
    pass

class InvalidEmailException(PostalException):
    pass