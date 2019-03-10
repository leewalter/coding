# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client

# Your Account Sid and Auth Token from twilio.com/console
account_sid = 'AC9xxxxxxxxxxxxxxxxxxxxxxxxxxxx99'
auth_token = '64xxxxxxxxxxxxxxxxxxxxxxxxxxx8'
client = Client(account_sid, auth_token)

phrases = [
    'hello',
    'hi',
    'Hello',
    'Hi there'
]

# Replace 'UAXXX...' with your Assistant's unique SID https://www.twilio.com/console/autopilot/list
for phrase in phrases:
    sample = client.autopilot \
        .assistants('UAxxxxxxxxxxxxxxxxxxxxxxxxxxxxxa') \
        .tasks('hello-world') \
        .samples \
        .create(language='en-us', tagged_text=phrase)

    print(sample.sid)
