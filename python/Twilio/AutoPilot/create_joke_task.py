# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client

# Your Account Sid and Auth Token from twilio.com/console
account_sid = 'AC9xxxxxxxxxxxxxxxxxxxxxxxxxxxx99'
auth_token = '64xxxxxxxxxxxxxxxxxxxxxxxxxxx8'
client = Client(account_sid, auth_token)

# Provide actions for the new task
joke_actions = {
    'actions': [
        {'say': 'I was going to look for my missing watch, but I could never find the time.'}
    ]
}

# Create a new task named 'tell_a_joke'
# Replace 'UAXXX...' with your Assistant's unique SID https://www.twilio.com/console/autopilot/list
task = client.autopilot \
    .assistants('UAxxxxxxxxxxxxxxxxxxxxxxxxxxxxxa') \
    .tasks \
    .create(
        unique_name='walter-tell-a-joke',
        actions=joke_actions)

print("Tell-a-joke task has been created!")
print(task.sid)
