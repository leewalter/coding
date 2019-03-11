'''
this is to ping a list of hosts to see if they are live or dead !
can also use python paramiko module if like to test ssh ok
netmiko will work fine too if use ssh to connect and test more
e.g.
https://github.com/ktbyers/netmiko/blob/develop/examples/simple_connection/simple_conn.py

'''
import os, sys, re

# if list from host1 to host100, then can generate them with list comprehension,
#sample_host_list = [ "host"+str(i) for i in range(1,100)]
#print(sample_host_list)

hostlist = ["www.google.com", "www.yahoo.com", "www.nosuchxyz.com"]
loss_regex = re.compile(r'(\(0% loss\))')  # any worst than "(0% loss)" is considered failure !

def islive(h):
    outfile = " > ping_result.txt"
    cmd="ping -n 1 " + h + outfile # save ping -n 1 <hostname> outputs to match in regex later
    #print(cmd)
    status_code = os.system(cmd)
    #print(type(status_code))
    #print("status_code is " , status_code)
    return (status_code) # return integer status = 0 if ping runs ok, = 1 if no such DNS, etc, errors

for i in range(len(hostlist)):

    if islive(hostlist[i]) == 1:
        #something wrong, e.g. no DNS name, failure, will flag and no need to match regex
        print("host at ", hostlist[i], " is not normal. ping status code not ok , please check !")

    else: # status_code == 0, so check regex if any match

        with open("ping_result.txt") as f:
            result = f.read()
            match = loss_regex.findall(result)
            #print(match)
            #print(len(match))
            if len(match) > 0:  # good if a match to "(0% loss)"
                print("host at ", hostlist[i], " ping is good : ",  match[0])
            else: # found NO match for (0% loss)
                print("host at ", hostlist[i], " ping is NOT good : ")

'''
case 1: when ping is good, status code = 0
e.g.
ping -n yahoo.com 

Pinging atsv2-fp-shed.wg1.b.yahoo.com [2001:4998:44:41d::3] with 32 bytes of data:
Reply from 2001:4998:44:41d::3: time=63ms 

Ping statistics for 2001:4998:44:41d::3:
    Packets: Sent = 1, Received = 1, Lost = 0 (0% loss),  <-- check this if live and ok !
Approximate round trip times in milli-seconds:
    Minimum = 63ms, Maximum = 63ms, Average = 63ms

case 2: when unable to ping, status code = 1
e.g.
Ping request could not find host www.nosuchxyz.com. Please check the name and try again.

so above will list ,

D:\Python\Python37-32\python.exe D:/Go-workspace/walter/coding/python/pinghosts.py
['host1', 'host2', 'host3', 'host4', 'host5', 'host6', 'host7', 'host8', 'host9', 'host10', 'host11', 'host12', 'host13', 'host14', 'host15', 'host16', 'host17', 'host18', 'host19', 'host20', 'host21', 'host22', 'host23', 'host24', 'host25', 'host26', 'host27', 'host28', 'host29', 'host30', 'host31', 'host32', 'host33', 'host34', 'host35', 'host36', 'host37', 'host38', 'host39', 'host40', 'host41', 'host42', 'host43', 'host44', 'host45', 'host46', 'host47', 'host48', 'host49', 'host50', 'host51', 'host52', 'host53', 'host54', 'host55', 'host56', 'host57', 'host58', 'host59', 'host60', 'host61', 'host62', 'host63', 'host64', 'host65', 'host66', 'host67', 'host68', 'host69', 'host70', 'host71', 'host72', 'host73', 'host74', 'host75', 'host76', 'host77', 'host78', 'host79', 'host80', 'host81', 'host82', 'host83', 'host84', 'host85', 'host86', 'host87', 'host88', 'host89', 'host90', 'host91', 'host92', 'host93', 'host94', 'host95', 'host96', 'host97', 'host98', 'host99']
host at  www.google.com  ping is good :  0% loss
host at  www.yahoo.com  ping is good :  0% loss
host at  www.nosuchxyz.com  is not normal. ping status code not ok , please check !
'''