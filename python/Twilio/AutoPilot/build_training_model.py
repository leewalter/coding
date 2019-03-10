# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
account_sid = 'AC9xxxxxxxxxxxxxxxxxxxxxxxxxxxx99'
auth_token = '64xxxxxxxxxxxxxxxxxxxxxxxxxxx8'
client = Client(account_sid, auth_token)

model_build = client.autopilot \
                    .assistants('UAxxxxxxxxxxxxxxxxxxxxxxxxxxxxxa') \
                    .model_builds \
                    .create(unique_name='v0.5')

print(model_build.sid)
