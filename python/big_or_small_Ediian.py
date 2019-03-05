'''
to determine big or small Ediian
https://stackoverflow.com/questions/1346034/whats-the-most-pythonic-way-of-determining-endianness

'''

import sys
print(sys.byteorder)

'''
on windows 10:
D:\Python\Python37-32\python.exe C:/Users/cheer/.PyCharmCE2018.2/config/scratches/scratch_28.py
little

on GCP:
1/ Debian:
cloudshell:~ (walter-terraform)$ uname -a
Linux cs-6000-devshell-vm-9fc15f81-907b-4d75-870d-f33a05c4b678 4.14.83+ #1 SMP Mon Feb 11 22:55:51 PST 2019 x86_64 GNU/Linux

cloudshell:~ (walter-terraform)$ python check_ediian.py
little

2/ Container-Optimized OS 74-11836.0.0 dev
Kernel: ChromiumOS-4.14.102 Kubernetes: 1.13.3 Docker: 18.09.1 Family: cos-dev
also little as above ! 
'''
