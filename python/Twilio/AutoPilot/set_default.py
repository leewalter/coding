# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
account_sid = 'AC9xxxxxxxxxxxxxxxxxxxxxxxxxxxx99'
auth_token = '64xxxxxxxxxxxxxxxxxxxxxxxxxxx8'
client = Client(account_sid, auth_token)

defaults = client.autopilot \
                 .assistants('UAxxxxxxxxxxxxxxxxxxxxxxxxxxxxxa') \
                 .defaults() \
                 .update(defaults={
                      'defaults': {
                          'assistant_initiation': 'task://hello-world',
                          'fallback': 'task://hello-world'
                      }
                  })

print(defaults.assistant_sid)
