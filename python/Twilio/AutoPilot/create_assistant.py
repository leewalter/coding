# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
account_sid = 'AC9xxxxxxxxxxxxxxxxxxxxxxxxxxxx99'
auth_token = '64xxxxxxxxxxxxxxxxxxxxxxxxxxx8'
client = Client(account_sid, auth_token)

assistant = client.autopilot \
                  .assistants \
                  .create(
                       friendly_name='Walter Quickstart Assistant',
                       unique_name='walter-quickstart-assistant'
                   )

print(assistant.sid)

'''
print(assistant.sid) = UAxxxxxxxxxxxxxxxxxxxxxxxxxxxxxa
'''