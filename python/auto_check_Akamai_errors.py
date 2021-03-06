# auto check Akamai real time errors via Akamai API
import os, sys 
import time, datetime
import json
from twilio.rest import Client

# Your Account Sid and Auth Token from twilio.com/console; should use env. file below if PROD, this is a quick test in 10min below
account_sid = 'ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
auth_token = '6xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
client = Client(account_sid, auth_token)

def twilio_send_sms(EdgeErrorPercent):

    if ( EdgeErrorPercent > 10 ):  # if error % > 10%, then send SMS for Alert ! 
        smsbody="Alert ! Site www.abc.com Edge Error % is high at " + str(EdgeErrorPercent) + "%!"
        #print (smsbody)
   
        message = client.messages.create(
                            body=smsbody,
                            from_='+17xxxxxxxxxx',
                            to='+14xxxxxxxxxxxxx'
                        )
        print(message.sid)


def current_time():
    ts = time.time()
    ts = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    print(ts)

def check_akamai_errors():
    # below will call Akamai API to get back current errors stats for a CPcode config
    cmd="http  --auth-type edgegrid -a default: --timeout=120  :/diagnostic-tools/v2/cpcodes/1234567890/estats > Akamai_error.txt" 
    returned_value = os.system(cmd)  # returns the exit code in unix, can do more error checking
    # print('returned value:', returned_value)

while True:
    current_time()
    check_akamai_errors()
    with open("D:/Akamai/api-kickstart/Akamai_error.txt") as f:
        json_results = f.read()
        json_dict = json.loads(json_results)
    # Save the EdgeFailurePercentage name into a variable; need to do more errors handling later
    edgeFailurePercentage_value = json_dict["eStats"]["edgeFailurePercentage"]
    originFailurePercentage_value = json_dict["eStats"]["originFailurePercentage"]
    # Print the errors %
    print ("edgeFailurePercentage_value: %10s" %(edgeFailurePercentage_value))
    print ("originFailurePercentage_value: %10s" %(originFailurePercentage_value))
    #edgeFailurePercentage_value=40 # fake a 40% error to test SMS
    twilio_send_sms(edgeFailurePercentage_value) 
    time.sleep(120)

'''
D:\Akamai\api-kickstart>python auto_check_Akamai_errors.py
2019-01-12 17:58:26
edgeFailurePercentage_value:        0.0
originFailurePercentage_value:        0.0
2019-01-12 18:01:42
edgeFailurePercentage_value:        0.0
originFailurePercentage_value:        0.0
2019-01-12 18:04:55
'''
