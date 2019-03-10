# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
account_sid = 'AC9xxxxxxxxxxxxxxxxxxxxxxxxxxxx99'
auth_token = '64xxxxxxxxxxxxxxxxxxxxxxxxxxx8'
client = Client(account_sid, auth_token)

# Replace 'UAXXX...' with your Assistant's unique SID https://www.twilio.com/console/autopilot/list
query = client.preview.understand \
                      .assistants('UAxxxxxxxxxxxxxxxxxxxxxxxxxxxxxa') \
                      .queries \
                      .create(language='en-US', query='Tell me a joke')

print(query.results.get('task'))
