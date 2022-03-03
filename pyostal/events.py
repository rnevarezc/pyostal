"""
The Events module:
Support for the different events a Postal Server could provide (usually via webhooks)
"""

from dataclasses import dataclass, field
from pyostal.exceptions import InvalidEventPayloadException
from pyostal.message import Message
from abc import abstractmethod

class EventInterface():
    # Message Events
    SENT = 'Sent'
    DELAYED = 'Delayed'
    DELIVERY_FAILED = 'DeliveryFailed'
    HELD = 'Held'
    BOUNCED = 'Bounced'
    LINK_CLICKED = 'LinkClicked'

    #Server Events
    SEND_LIMIT_EXCEEDED = 'SendLimitExceeded'
    SEND_LIMIT_APPROACHING = 'SendLimitApproaching'
    DOMAIN_DNS_ERROR = 'DomainDNSError'

    @abstractmethod
    def get_type(self) -> str: raise NotImplementedError

@dataclass
class HasMessageMixin:
    message: Message

    def __post_init__(self):
        self.message = Message.from_payload(self.message)

@dataclass
class HasStatusMixin(HasMessageMixin):
    status: str
    details: str
    output: str
    time: float
    sent_with_ssl: bool
    timestamp: float

@dataclass
class MessageDeliveryFailed(HasStatusMixin, EventInterface):
    def get_type(self) -> str: return EventInterface.DELIVERY_FAILED

@dataclass
class MessageHeld(HasStatusMixin, EventInterface):
    def get_type(self) -> str: return EventInterface.HELD

class MessageSent(HasStatusMixin, EventInterface):
    def get_type(self) -> str: return EventInterface.SENT

class MessageDelayed(HasStatusMixin, EventInterface):
    def get_type(self) -> str: return EventInterface.DELAYED

@dataclass
class MessageBounced(EventInterface):        
    bounce: Message
    message: Message = field(init=False)
    original_message: Message

    def __post_init__(self):
        self.message = Message.from_payload(self.original_message)
        self.bounce = Message.from_payload(self.bounce)
    
    def get_type(self) -> str: return EventInterface.BOUNCED

@dataclass
class MessageLinkClicked(HasMessageMixin, EventInterface):
    url: str
    token: str
    ip_address: str
    user_agent: str
    
    def get_type(self) -> str: return EventInterface.LINK_CLICKED

@dataclass
class HasServerMixin:
    server: dict

    def get_server_id(self):
        return self.server['uuid']

@dataclass
class SendLimitExceeded(HasServerMixin, EventInterface):
    volume: int
    limit: int
    
    def get_type(self) -> str: return EventInterface.SEND_LIMIT_EXCEEDED

@dataclass
class SendLimitApproaching(HasServerMixin, EventInterface):
    volume: int
    limit: int

    def get_type(self) -> str: return EventInterface.SEND_LIMIT_APPROACHING

@dataclass
class DomainDNSError(HasServerMixin, EventInterface):
    domain: str
    uuid: str
    dns_checked_at: float
    spf_status: str
    spf_error: str
    dkim_status: str
    dkim_error: str
    mx_status: str
    mx_error: str
    return_path_status: str
    return_path_error: str

    def get_type(self) -> str: return EventInterface.DOMAIN_DNS_ERROR

class EventFactory:
    """ Static class for building different types of events depending
    of the provided Payload
    """
    @staticmethod
    def build(payload: dict) -> EventInterface:
        try:
            # Try to get the class definition
            class_ = globals()[payload['event']]
            data = payload['payload']

            if payload['event'] == 'DomainDNSError':
                # DomainDNSError has a 'message' key nested in the payload
                # it is necessary to hack the data here.
                data = payload['payload']['message']
            
            return class_(**data)
        except Exception as e:
            # This would be very strange, but we must be prepared.
            # (Maybe a weird payload was supplied?)
            raise InvalidEventPayloadException('Invalid Payload provided')