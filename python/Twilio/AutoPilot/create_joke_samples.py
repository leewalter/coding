# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client

# Your Account Sid and Auth Token from twilio.com/console
account_sid = 'AC9xxxxxxxxxxxxxxxxxxxxxxxxxxxx99'
auth_token = '64xxxxxxxxxxxxxxxxxxxxxxxxxxx8'
client = Client(account_sid, auth_token)

phrases = [
    'Tell me a joke',
    'Tell me a joke',
    'I\'d like to hear a joke',
    'Do you know any good jokes?',
    'Joke',
    'Tell joke',
    'Tell me something funny',
    'Make me laugh',
    'I want to hear a joke',
    'Can I hear a joke?',
    'I like jokes',
    'I\'d like to hear a punny joke'
]

# Provide actions for the new task
joke_actions = {
    'actions': [
        {'say': 'What is the best thing about Switzerland ? I do not know, but the flag is a big plus !'}
    ]
}


# Replace 'UAXXX...' with your Assistant's unique SID https://www.twilio.com/console/autopilot/list
# Replace 'UDXXX...' with the SID for the task you just created.
for phrase in phrases:
    sample = client.autopilot \
        .assistants('UAxxxxxxxxxxxxxxxxxxxxxxxxxxxxxa') \
        .tasks('walter-tell-a-joke') \
        .samples \
        .create(language='en-us', tagged_text=phrase)

    print(sample.sid)

'''
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
'''