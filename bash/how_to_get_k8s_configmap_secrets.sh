# https://kubernetes.io/docs/tasks/configure-pod-container/configure-pod-configmap/
#ref - http://k8s.cookbook.fyi/ch08/
#how to use k8s configmap to store and pass secret
# a/ from-literal
# b/ from a file 

#a/ from-literal

kubectl create configmap siseconfig --from-literal=siseversion=0.9
configmap/siseconfig created

#b/ from file 

$ kubectl create configmap configfile --from-file=example.cfg
configmap/configfile created
$ kubectl get configmap
NAME         DATA      AGE
configfile   1         9s
siseconfig   1         1m

# vi cmconsumer.yaml ; see http://k8s.cookbook.fyi/ch08/cmconsumer.yaml

apiVersion:       v1
kind:             Pod
metadata:
  name:           oreilly
spec:
  containers:
  - image:        busybox
    command:
    - sleep
    - "3600"
    volumeMounts:
    - mountPath:  /oreilly
      name:       oreilly
    name:         busybox  
  volumes:
  - name:
    configMap:
      name:       configfile
      

$ kubectl apply -f cmconsumer.yaml
pod/oreilly created

$ kubectl exec -ti oreilly -- ls -l /oreilly
total 0
lrwxrwxrwx    1 root     root            18 Feb  5 01:52 example.cfg -> ..data/example.cfg

$ kubectl exec -ti oreilly -- cat /oreilly/example.cfg
debug: true
home: ~/abc
key1: walter
key2: lee     


$ kubectl get po
NAME                                READY     STATUS    RESTARTS   AGE
oreilly                             1/1       Running   0          13m
ppconsumer                          1/1       Running   0          49m

$ kubectl get configmap
NAME         DATA      AGE
configfile   1         18m
siseconfig   1         19m

$ kubectl get secrets
NAME                  TYPE                                  DATA      AGE
default-token-tv6gr   kubernetes.io/service-account-token   3         1h
pp                    Opaque                                1         51m
