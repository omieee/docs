# K2 architecture, use step on kind (Claude) · 2026-11-13 · W6

- Type: unscored teaching check (use step after the KodeKloud CKA lesson "Cluster Architecture", 08:48). Not a unit proof; K2's proof is the narrative, no notes, 7/10.
- Context: Om chose to follow the KodeKloud CKA course order (12:37); batch item 13 in `claude/plan-drafts/2026-11-15-batch.md`.
- Before: `-o yaml` taught on `k1-interview` (spec = what you asked for, status = what is happening, written by Kubernetes); Om found the fields Kubernetes added (`name: web` was his own); spec vs status clear (12:37).

## Question as asked (12:56)

Run `kubectl get pods -n kube-system -o wide`. Leave out coredns and kindnet. For etcd, kube-apiserver, kube-controller-manager, kube-proxy and kube-scheduler: what it does in a few words, and control plane or worker. Then name the one component from the video that is not in the list.

## Om's answer, verbatim (13:39)

> etcd will store all the information and status about container, pods in a key value pair. That is the datbase of that cluster and it's components
> kube-apiserver . that exposes multiple api endpoints to controll the cluster .. kubectl command most probably should be issues it to this component
> kube-controller: this cordinate with otjher contyroller like node-controller to get their respective work done
> kube-proxy: this is used to communicate between containers
> scheduler: this schedules node and make is ready to deply containers on thiose .. taint, tolleration are taken care of

## Feedback given (13:42)

- etcd right; apiserver right; kube-proxy right at the video's level.
- Controller manager close: many controllers run inside it, each watches the cluster and fixes it back to what was asked (node controller example).
- Scheduler: wrong direction. It picks a node for each new pod and writes `nodeName` (the line Om saw in his `-o yaml` and never wrote); it does not prepare nodes or start containers.
- Not answered: control plane vs worker split, and the missing component. Given: kubelet is missing; scheduler picks, kubelet does. Control plane: etcd, apiserver, controller manager, scheduler; every worker: kubelet, kube-proxy, container runtime.
- Om (23:32): "YEs clear".
