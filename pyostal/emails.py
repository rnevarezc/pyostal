from pydantic.dataclasses import dataclass
from dataclasses import field
from .response import Response
from .exceptions import InvalidEmailException
from base64 import b64encode
from copy import copy

class HasMessagesMixin:
    message_id: str
    messages: list = []

    def set_response(self, response: Response):
        self.message_id = response.data.get('message_id')
        self.messages = response.data.get('messages')

@dataclass
class Email(HasMessagesMixin):
    """
    A Data Structure Class to handle the Email payload.
    """
    from_address: str
    subject: str
    to: list[str] = field(default_factory=list)
    cc: list[str] = field(default_factory=list)
    bcc: list[str] = field(default_factory=list)
    plain_body: str = None
    html_body: str = None
    reply_to: str = None
    attachments: list[str] = field(default_factory=list)
    headers: dict = field(default_factory=dict)

    def __post_init__(self):
        if not self.to and not self.cc and not self.bcc:
            raise InvalidEmailException('Email must have at least one recipient')
        if not self.plain_body and not self.html_body:
            raise InvalidEmailException('Email must have a plain_body or html_body')
        return

    def add_attachment(self, filename: str, content_type: str, data: str):
        self.attachments.append({
            'name': filename,
            'content_type': content_type,
            'data': b64encode(data),
        })

    def add_to(self, to: str): self.to.append(to)

    def add_cc(self, cc: str): self.cc.append(cc)

    def add_bcc(self, bcc: str): self.bcc.append(bcc)

    def add_header(self, header: dict): self.headers.append(header)

    def as_payload(self) -> dict :
        """ Get the Email data as a payload to be sent to the Postal API """

        # We MUST copy the self dict, otherwise the variable is referenced
        payload = copy(self.__dict__)

        # Necessary to add the from key (reserved keyword) to the json payload.
        payload['from'] = payload['from_address']
        del payload['from_address']

        return payload
