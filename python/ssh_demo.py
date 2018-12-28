# ref at https://gist.github.com/leewalter/17753a18495095e1ef8768fe3c761869
#!/usr/bin/env python

import sys, paramiko

if len(sys.argv) < 4:
    print("args missing")
    sys.exit(1)

hostname = sys.argv[1]
password = sys.argv[2]
command = sys.argv[3]

username = "luckywalter"
port = 22

try:
    client = paramiko.SSHClient()
    client.load_system_host_keys()
# see doc at http://docs.paramiko.org/en/2.4/api/client.html  for missing host key policies  
#    client.set_missing_host_key_policy(paramiko.WarningPolicy)
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy)

    client.connect(hostname, port=port, username=username, password=password)

    stdin, stdout, stderr = client.exec_command(command)
    print("*** Here we go!\n")
    out1=stdout.read(),
    print(out1)


finally:
    client.close()
