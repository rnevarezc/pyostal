# PYostal: Postal API Client

This library helps you use the [Postal](https://github.com/atech/postal) API in Python 3.9 (and above) to send Emails, get Message Details & Deliveries and Implement Events to handle Server Webhooks.

It uses [Requests](https://github.com/psf/requests) the simple, yet elegant HTTP library to handle all the http sorcery.

## Installing Requests and Supported Versions

PYostal is available on PyPI:

```bash
$ python -m pip install pyostal
```
PYostal officially supports Python 3.9+.

## Usage

### Using the Client

You will need an API Credential from your Postal Installation to use the API Client.

```python
from pyostal.client import Client

# Create a new Postal client using the server key of your Postal Installation.
client = Client('https://postal.yourdomain.com', 'your-api-key')

# Optional: You can add any aditional Headers for your API installation
# (Maybe Authorization)
# You just add a dict with your headers:
headers = {
    'Authorization' => 'Basic RTYtaO54BGBtcG9yYWwyMDIw'
}

client = Client('https://postal.yourdomain.com', 'your-api-key', headers)

#Or you can add them manually to a Client Instance:
client.headers = headers
```

### Sending an Email

Sending an email is simple. You can follow the example below:

```python
# Create a dict with the message:
payload = {
    'to': ['mail@example.com'],
    'from_address': 'othermail@example.com',
    'reply_to': 'reply-to@example.com',
    'subject': 'This is a subject',
    'plain_body': 'This is a body'
}

#send it using the client. that's it
response = client.send(payload)
```
Or Create a new Email instance and add manually each of the Mail attributes
```python

from pyostal.emails import Email

email = Email({
    'to': ['mail@example.com'],
    'bcc': ['test1@example.com', 'test2@example.com],
    'from_address': 'othermail@example.com',
    'reply_to': 'reply-to@example.com',
    'subject': 'This is a subject',
    'plain_body': 'This is a body'
})

email.add_cc('emailcc@example.com')
email.html_body = "<p>This is a HTML body</p>"

# Here we get a pyostal.response.Response instance
response = client.send(Email)
```
## API Information

You can get more information about the Postal API and Payloads in the [Postal Project Wiki](https://github.com/postalhq/postal/wiki/Using-the-API)

## Author

Rafael Nevarez
