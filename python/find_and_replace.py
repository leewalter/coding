# simple python code to search dir, do a regex matching and replace a variable
'''
example use case - k8s yaml file , search for pod selector = "stg", then replace it to "PROD" to select new pods
'''

import sys
import os
import glob
# import re
import fileinput

for filename in glob.glob("test/*.yaml"):
  with fileinput.FileInput(filename, inplace=True, backup='.bak') as file:
     for line in file:
        print(line.replace('stg', 'PROD'), end='')
        
'''
output:
====================================================
before:

apiVersion: apps/v1 # for versions before 1.9.0 use apps/v1beta2
kind: Deployment
metadata:
  name: nginx-deployment
spec:
  selector:
    matchLabels:
      app: nginx
      env: stg  <---
  replicas: 2 # tells deployment to run 2 pods matching the template
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx:1.7.9
        ports:
        - containerPort: 80
====================================================
after:

apiVersion: apps/v1 # for versions before 1.9.0 use apps/v1beta2
kind: Deployment
metadata:
  name: nginx-deployment
spec:
  selector:
    matchLabels:
      app: nginx
      env: PROD  <-- changed pod selector !
  replicas: 2 # tells deployment to run 2 pods matching the template
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx:1.7.9
        ports:
        - containerPort: 80

'''        
