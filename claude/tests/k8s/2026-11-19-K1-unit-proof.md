# K1 Cluster and architecture: unit proof, cold (Claude) · 2026-11-19 · W7

- Type: unit proof (section 7: artifact, lab evidence, one paragraph from memory, three cold questions from the ladder). K1's own bar (section 6.3): each component in the lessons found where it runs on kind, a Pod in `kube-system` or kubelet as a process on the node, and explained in one line, cold.
- Artifact and lab evidence: docs PR #3 `75e47e3`, `k8s/k8s-notes.md`: `kubectl get pods -n kube-system -o wide` output (all on `phase1-k1-control-plane`) and `docker exec phase1-k1-control-plane systemctl status kubelet` output (kubelet.service active, PID 209). Pasted terminal output inside a commit (evidence order (c)); kind cannot run in Claude's container. K1 part 1 (kind cluster and first pod) done Oct 26 with ChatGPT.
- Taught before (checked): KodeKloud CKA Core Concepts lessons Cluster Architecture, Docker vs containerd, etcd for Beginners, etcd in Kubernetes, Kube API Server, Kube Controller Manager, Kube Scheduler, Kubelet, Kube Proxy (Om's screenshots Nov 17 and Nov 18); Nov 13 use step (control plane vs worker split, scheduler picks and kubelet does, kubelet missing from the list); Nov 19 notes review (kube-proxy is Service traffic to Pods; kubelet must run before Pods). coredns and kindnet not taught, so left out.
- Timing: Om said 'ready' 13:06, straight after the notes (Claude had suggested lunch first; Om's call). Questions sent about 13:10. Plan box about 15 minutes (section 7).
- Scoring set before the answer (written 13:09, before sending):
  - Part A, the paragraph (K1's own bar): six components, each right if both what it does and where it runs on kind are right. Bar: at least 5 of 6 right and none inverted (for example kubelet as a Pod, or the scheduler starting containers).
  - Q1 Mechanism (0-2): 2 = kubectl to apiserver, Pod saved in etcd; scheduler sees a Pod with no node, picks one, the choice goes back through the apiserver; kubelet on that node sees the Pod, has containerd start the container, reports status back to the apiserver. 1 = order right with one component skipped, or a component talking to etcd directly. 0 = scheduler or apiserver starts the container, or the order inverted.
  - Q2 Failure (0-2): 2 = running Pods keep running (kubelet keeps them up), the new Pod is saved but gets no node and never starts, plus one way to notice (`kubectl get pods` shows it not running or Pending, `describe` shows no node, or the scheduler Pod not Running in kube-system). 1 = one half right, or no way to notice. 0 = running Pods stop.
  - Q3 Transfer (0-2): 2 = control plane node: etcd, kube-apiserver, kube-controller-manager, kube-scheduler (and its own kube-proxy); each worker: kube-proxy only; kubelet a program on every node, not in the list. 1 = one slip. 0 = control plane Pods on workers, or kubelet as a Pod.
  - Ladder bar: 4/6 or better (the 6-7/10 working-recall calibration) and no wrong conclusion. K1 PASS = Part A bar met and ladder bar met. A miss is taught on the spot, then one fresh retry (section 0 step 5).

## Questions as asked

**Part A. One paragraph from memory.** Name the six components from the lessons: etcd, kube-apiserver, kube-controller-manager, kube-scheduler, kube-proxy, kubelet. For each one, say in one line what it does and where it runs on your kind cluster: as a Pod in `kube-system`, or as a program on the node.

**Q1. Step by step.** A cluster has one control plane node and two worker nodes. You run `kubectl run web --image=nginx`. Which components act, in what order, until the nginx container is running on a worker?

**Q2. What breaks.** On that same cluster, kube-scheduler stops working. What happens to the Pods that are already running? What happens to a new Pod you create now? How would you notice?

**Q3. A new case.** On that same 3-node cluster you run `kubectl get pods -n kube-system -o wide`. Leave out coredns and kindnet. Which Pods would you see on a worker node? Which only on the control plane node? Where is kubelet?

Start each answer with an "Asked:" line, as in the 875 habit.

## Om's answer, verbatim (13:23)

> 1.
>    1. etcd: (CP-pod) is the source of truth (database) where every details for that cluster are stored.
>    2. ka: (CP-pod) is the component that talks with other component it is the only one that talks to etcd .. kubectl commands are entertained byu him
>    3. kcm: (CP-pod) ths is teh process which hold many other controllers and those controller makes sure the desired state is maintained
>    4. ks: (CP-pod) : it understands the pods requirements and sees which node will be fit and assigns the node to which that pod should get deployed on by kubelet ... it just assigns
>    5. kube-proxy(Worker pod): it in communication with the help of services and allows services to forward the traffic to pod
>    6. kubelet(worker, process): this guy is the one that along with containerd  deploys the pods on the designated node
> 2. first the request goes to api server that check the etcd and adds the entry that the pod should be created then secheduler check the pods requirement and finds out the which node and asks api-servcer to add that node entry in the pod description .. that is read ksn's node-controller that preps the node and once the node is ok kubelet along with conmtainerd pull the nginx image and deploys the nginx pod and and priovides status back to api-server ..
> 3. already running pod will be fine but new pods can't be deployed becvause which node to go is not known
> 4. kube-proxy will see on worker node , all other on CP .. kubelet is the service running within docker in this case as a part of service

(Om's 1 is Part A, his 2-4 are Q1-Q3. About 13m elapsed, questions about 13:10, answer 13:23; no start time and no 'Asked:' lines.)

## Scores (cold)

- Part A 6/6 right, none inverted: bar met. Each component's job right, and where it runs right (four control plane Pods, kube-proxy a Pod, kubelet a process). K1's own bar (section 6.3) is met.
- Q1 Mechanism 1/2. Right: apiserver first and the Pod saved in etcd; the scheduler picks the node and has the apiserver write it into the Pod (through the apiserver, not to etcd directly); kubelet with containerd pulls and starts, status back to the apiserver. Wrong: 'that is read [by kcm's] node-controller that preps the node and once the node is ok kubelet...': the node controller is not in this chain (it watches node health); nothing prepares the node per Pod. Missing: how kubelet learns of the Pod (it watches the apiserver for Pods given to its node).
- Q2 Failure 1/2. Both halves right with the reason ('which node to go is not known'). 'How would you notice?' not answered.
- Q3 Transfer 1/2. Worker: kube-proxy, right; control plane only: 'all other', right. kubelet: 'the service running within docker in this case' says a service, not a Pod, but not where on the 3-node cluster (every node, three kubelets). Claude's part: Claude's Nov 13 summary said 'every worker: kubelet, kube-proxy', loose wording, and at 13:05 today let the '(Worker)' tags stand as polish; logged as a coach error.
- Ladder 3/6, below the 4/6 bar set before the answer. Cold verdict: PARTIAL (Part A passed, ladder short). Teaching on the spot and one fresh retry per item follow.
