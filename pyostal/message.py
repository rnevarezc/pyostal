from dataclasses import dataclass
from typing import Optional, Dict

@dataclass
class Message:
    """
    A Data Structure Class to handle the Postal Message payload.

    Attributes:
    ----------
    id: int
        The integer ID of the message
    token: str
        The unique token of the message
    direction: str
        Direction of the message: Incoming | Outgoing
    message_id: str
        Unique ID of the associated message
    to: str
        The Recipient email address 
    from_: str
        The sender email address 
    timestamp: float 
        The message timestamp
    spam_status: str
        The email spam status: Spam | NotSpam
    tag: str, optional
        A tag assigned to the message.
    status: dict, optional
        Optional data of the message current status
    details: dict, optional
        Optional details of the message.
    """

    id: int
    token: str
    direction: str
    message_id: str
    to: str
    from_: str
    subject: str
    timestamp: float
    spam_status: str
    tag: Optional[str] = None
    status: Optional[Dict] = None
    details: Optional[Dict] = None

    @staticmethod
    def from_payload(payload: dict):
        """ 
        A necessary helper method to parse the 'from' attribute 
        (reserved keyword) in the original payload provided by the Postal API
        """ 
        payload['from_'] = payload['from']
        del payload['from']
        return Message(**payload)