# ref - http://k8s.cookbook.fyi/ch08/
# try to pass API access key to a Pod using a "secret"
# assume a k8s secret already added , see http://k8s.cookbook.fyi/ch08/ppconsumer.yaml
#   echo -n "open sesame" > ./passphrase
#   kubectl create secret generic pp --from-file=./passphrase
#   kubectl describe secrets/pp

# then create a pod to get it out
# kubectl create -f ppconsumer.yaml ; see http://k8s.cookbook.fyi/ch08/ppconsumer.yaml
# kubectl logs ppconsumer
#   tmpfs on /tmp/access type tmpfs (ro,relatime)

$ kubectl exec ppconsumer -i -t -- sh
/ # cat /tmp/access/passphrase
open sesame/

$ kubectl get secret pp
NAME      TYPE      DATA      AGE
pp        Opaque    1         28m

$ kubectl get secret pp -o yaml
apiVersion: v1
data:
  passphrase: b3BlbiBzZXNhbWU=
kind: Secret
metadata:
  creationTimestamp: 2019-02-05T01:15:11Z
  name: pp
  namespace: default
  resourceVersion: "520"
  selfLink: /api/v1/namespaces/default/secrets/pp
  uid: 7c45ad44-28e3-11e9-aeb0-0242ac11000a
type: Opaque

$ kubectl get secret pp -o yaml | grep passphrase | cut -d":" -f 2 | awk '{$1=$1};1' | base64 --decode
open sesame$
  
  
