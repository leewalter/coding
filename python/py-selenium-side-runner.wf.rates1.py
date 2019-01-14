# python to schedule and run it once an hour with "selenium-side-runner www-mortgage-rate1.side"

import time, os

def check_wf_rates():
    # below will call selenium-side-runner www-mortgage-rate1.side to see current WF mortgage rates for CA - San Francisco county new purpose
    cmd="selenium-side-runner www-mortgage-rate1.side" 
    returned_value = os.system(cmd)  # returns the exit code in unix/windows
    # print('returned value:', returned_value)

while True:
    check_wf_rates()
    time.sleep(3600)
    
'''
sample video at
https://www.linkedin.com/feed/update/urn:li:activity:6490390335695527936

D:\Akamai\api-kickstart>python py-selenium-side-runner.wf.rates1.py
info:    Running www-mortgage-rate1.side

 RUNS  ./Default Suite.test.js

 RUNS  ./Default Suite.test.js
 RUNS  ./Default Suite.test.js
 PASS  ./Default Suite.test.js (32.994s)
  Default Suite
    √ wf-mortgage-rates1 (26779ms)

Test Suites: 1 passed, 1 total
Tests:       1 passed, 1 total
Snapshots:   0 total
Time:        33.389s, estimated 41s
Ran all test suites.
<will repeat again after 3600sec = 1hr>
...
