# k8s - Notes

## My Local instance

```
kubectl get pods -n kube-system -o wide

NAME                                              READY   STATUS    RESTARTS       AGE   IP           NODE                      NOMINATED NODE   READINESS GATES
coredns-559f6c778d-qc2tn                          1/1     Running   26 (23m ago)   23d   10.244.0.6   phase1-k1-control-plane   <none>           <none>
coredns-559f6c778d-xr2fr                          1/1     Running   26 (23m ago)   23d   10.244.0.2   phase1-k1-control-plane   <none>           <none>
etcd-phase1-k1-control-plane                      1/1     Running   26 (23m ago)   23d   172.18.0.2   phase1-k1-control-plane   <none>           <none>
kindnet-whcph                                     1/1     Running   26 (23m ago)   23d   172.18.0.2   phase1-k1-control-plane   <none>           <none>
kube-apiserver-phase1-k1-control-plane            1/1     Running   26 (23m ago)   23d   172.18.0.2   phase1-k1-control-plane   <none>           <none>
kube-controller-manager-phase1-k1-control-plane   1/1     Running   26 (23m ago)   23d   172.18.0.2   phase1-k1-control-plane   <none>           <none>
kube-proxy-v7xrs                                  1/1     Running   26 (23m ago)   23d   172.18.0.2   phase1-k1-control-plane   <none>           <none>
kube-scheduler-phase1-k1-control-plane            1/1     Running   26 (23m ago)   23d   172.18.0.2   phase1-k1-control-plane   <none>           <none>
```

## Kubernetes Components

- **etcd** (Control-Plane) : `etcd` is a key-value pair database. In kubernetes it hold all the details about the cluster, all componenets, pod state.. Basically it is the source of truth for that cluster
- **kube-apiserver** (Control-Plane): `kube-apiserver` is the component that communicates to all other components. It is the only component that conencts to `etcd`. when we issue a `kubectl` command. it goes to this component only and it then fetches the details from etcd and serve us.
- **kube-controller-manager** (Control-Plane): `kube-controller-manager` is the program that hold many other controllers. Each `controller` watches its own part of the cluster and fixes it back to the desired state.
- **kube-scheduler** (Control-Plane): `kube-scheduler` it just assigns which node the pod to go. based on the requirement the pod needs it see which node is best fit and assigns the pod to that node. _**Note**_: It doesnot do anything apart from allotment.
- **kube-proxy** (Worker): `kube-proxy` is the component that helps communication between the pods .. It communicates with the services and forwards the traffic to the actual pod.
- **kubelet** (Worker): `kubelet` is the component that actually with the help of `container-d` deploys the pod on scheduled node and monitiors the health and reoprts back to `kube-apiserver`. by efault `kubelet` is not installed in kind cluster as pod, but it runs as a program. we can view that by exec into it in docker.

```
docker exec -it phase1-k1-control-plane systemctl status kubelet

● kubelet.service - kubelet: The Kubernetes Node Agent
     Loaded: loaded (/etc/systemd/system/kubelet.service; enabled; preset: enabled)
    Drop-In: /etc/systemd/system/kubelet.service.d
             └─10-kubeadm.conf, 11-kind.conf
     Active: active (running) since Thu 2026-11-19 03:46:06 UTC; 1h 23min ago
 Invocation: 12b76ffa5a3a498cab1c6e47692339a3
       Docs: http://kubernetes.io/docs/
    Process: 198 ExecStartPre=/bin/sh -euc if [ -f /sys/fs/cgroup/cgroup.controllers ]; then /kind/bin/create-kubelet-cgroup-v2.sh; fi (code=exited, status=0/SUCCESS)
    Process: 207 ExecStartPre=/bin/sh -euc if [ ! -f /sys/fs/cgroup/cgroup.controllers ] && [ ! -d /sys/fs/cgroup/systemd/kubelet ]; then mkdir -p /sys/fs/cgroup/systemd/kubelet; fi (code=exited, status=0/SUCCESS)
   Main PID: 209 (kubelet)
      Tasks: 18 (limit: 3534)
     Memory: 48M (peak: 50.6M)
        CPU: 3min 22.452s
     CGroup: /kubelet.slice/kubelet.service
             └─209 /usr/bin/kubelet --bootstrap-kubeconfig=/etc/kubernetes/bootstrap-kubelet.conf --kubeconfig=/etc/kubernetes/kubelet.conf --config=/var/lib/kubelet/config.yaml --node-ip=172.18.0.2 --provider-id=kind://docker/phase1-k1/phase1-k1-control-plane --node-labels= --runtime-cgroups=/system.slice/containerd.service

Nov 19 03:46:26 phase1-k1-control-plane kubelet[209]: I1119 03:46:26.569467     209 server.go:177] "Pod update broadcasted" podUID="dd3868ca934e5e9cdd5f16457b971879" type="MODIFIED"
Nov 19 03:46:46 phase1-k1-control-plane kubelet[209]: I1119 03:46:46.369401     209 scope.go:118] "RemoveContainer" containerID="dd039da1369851cc74e11c4f500d8aeddaead0627cf3f2ab9090fb03bb7c3648"
Nov 19 03:46:46 phase1-k1-control-plane kubelet[209]: I1119 03:46:46.369922     209 server.go:177] "Pod update broadcasted" podUID="66342bae-b51b-4ca9-ba94-9215b356f208" type="MODIFIED"
Nov 19 03:46:46 phase1-k1-control-plane kubelet[209]: I1119 03:46:46.370321     209 scope.go:118] "RemoveContainer" containerID="bb40bab21721f86a96bc426184162b5f7d646c4b90e5dc9e867140d722d53983"
Nov 19 03:46:46 phase1-k1-control-plane kubelet[209]: E1119 03:46:46.370635     209 pod_workers.go:1338] "Error syncing pod, skipping" err="failed to \"StartContainer\" for \"local-path-provisioner\" with CrashLoopBackOff: \"back-off 10s restarting failed container=local-path-provisioner pod=local-path-provisioner-75f7fc7dc5-gwq7h_local-path-storage(66342bae-b51b-4ca9-ba94-9215b356f208)\"" pod="local-path-storage/local-path-provisioner-75f7fc7dc5-gwq7h" podUID="66342bae-b51b-4ca9-ba94-9215b356f208"
Nov 19 03:46:49 phase1-k1-control-plane kubelet[209]: I1119 03:46:49.216425     209 server.go:177] "Pod update broadcasted" podUID="a95e9cc5-40fc-4967-ae53-b454942b0189" type="MODIFIED"
Nov 19 03:46:54 phase1-k1-control-plane kubelet[209]: I1119 03:46:54.110841     209 server.go:177] "Pod update broadcasted" podUID="30c21234-c815-4b46-9938-cb8eb5f1b666" type="MODIFIED"
Nov 19 03:46:58 phase1-k1-control-plane kubelet[209]: I1119 03:46:58.128277     209 server.go:177] "Pod update broadcasted" podUID="66342bae-b51b-4ca9-ba94-9215b356f208" type="MODIFIED"
Nov 19 03:46:58 phase1-k1-control-plane kubelet[209]: I1119 03:46:58.129046     209 scope.go:118] "RemoveContainer" containerID="bb40bab21721f86a96bc426184162b5f7d646c4b90e5dc9e867140d722d53983"
Nov 19 03:46:58 phase1-k1-control-plane kubelet[209]: I1119 03:46:58.329670     209 server.go:177] "Pod update broadcasted" podUID="66342bae-b51b-4ca9-ba94-9215b356f208" type="MODIFIED"
```