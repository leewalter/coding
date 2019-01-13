# auto check Akamai real time errors via Akamai API
import os, sys 
import time, datetime
import json

def current_time():
    ts = time.time()
    ts = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    print(ts)

def check_akamai_errors():
    # below will call Akamai API to get back current errors stats for a CPcode config
    cmd="http  --auth-type edgegrid -a default: --timeout=120  :/diagnostic-tools/v2/cpcodes/123456789/estats > Akamai_error.txt" 
    returned_value = os.system(cmd)  # returns the exit code in unix
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
