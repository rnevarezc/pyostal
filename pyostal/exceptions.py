"""
Postal Common Exceptions

Several exceptions used to handle the API different responses.
"""

class PostalException(RuntimeError):
    pass

class InvalidRequestException(PostalException):
    pass

class InvalidEventPayloadException(PostalException):
    pass

class InvalidEmailException(PostalException):
    pass