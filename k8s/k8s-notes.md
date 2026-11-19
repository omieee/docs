# k8s - Notes

## Kubernetes Components

- **etcd** : `etcd` is a key-value pair database. In kubernetes it hold all the details about the cluster, all componenets, pod state.. Basically it is the source of truth for that cluster
- **kube-apiserver** : `kube-apiserver` is the component that communicates to all other components. It is the only component that conencts to `etcd`. when we issue a `kubectl` command. it goes to this component only and it then fetches the details from etcd and serve us.
- **kube-controller-manager** : `kube-controller-manager` is the componets that hold many other controllers and make sure the desired estate is achieved by all other controllers. It's like the manager of all other `controllers`
- **kube-scheduler** : `kube-scheduler` it just assigns which node the pod to go. based on the requirement the pod needs it see which node is best fit and assigns the pod to that node. _**Note**_: It doesnot do anything apart from allotment.
- **kube-proxy** : `kube-proxy` is the component that helps communication between the pods .. It communicates with the services and forwards the traffic to the actual pod.
- **kubelet** : `kubelet` is teh component that actually with the help of `container-d` deploys the pod on scheduled node and monitiors the health and reoprts back to `kube-apiserver`. by efault `kubelet` is not installed in kind cluster as pod 