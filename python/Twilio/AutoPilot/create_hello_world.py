# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client

# Your Account Sid and Auth Token from twilio.com/console
account_sid = 'AC9xxxxxxxxxxxxxxxxxxxxxxxxxxxx99'
auth_token = '64xxxxxxxxxxxxxxxxxxxxxxxxxxx8'
client = Client(account_sid, auth_token)

# Build task actions that say something and listens for a repsonse.
hello_world_task_actions = {
    'actions': [
        {'say': 'Hi there, I\'m your virtual assistant! How can I help you?'},
        {'listen': True}
    ]
}


# Create the hello_world task
# Replace 'UAXXX...' with your Assistant's unique SID https://www.twilio.com/console/autopilot/list
task = client.autopilot.assistants('UAxxxxxxxxxxxxxxxxxxxxxxxxxxxxxa') \
                       .tasks \
                       .create(
                           unique_name='hello-world',
                           actions=hello_world_task_actions)

print("Hello-world task has been created!")
print(task.sid)