# Kubernetes Self-Audit — 2026-09-24

Run cold. No cluster, no notes, no docs, no AI. Part of the Week 1 gate (`2_week_by_week.md`, W1: "K8s self-audit (1 hr) — the 10 debugging questions, cold, no notes, honest scoring").

**Candidate:** ~12 yrs SWE, 5 at IBM Cloud, production Kubernetes exposure via CDP.  
**Result: 2.5 / 10.**

---

**Q1. A pod is in `CrashLoopBackOff`. How do you diagnose it? What does `--previous` give you and why do you need it?**

_Answer given:_ "I will check the pod events. Why is it crashing. I think `--previous` gives me the previous config for that pod."

_Score: 0.5_  
Checking events is a reasonable first instinct. But `--previous` was wrong: it is a flag on `kubectl logs`, and it returns the **logs of the previous, crashed container instance**, not config. It is needed because the container has already restarted, so the current instance's logs are empty or near-empty. Without `--previous` you cannot see why it died. Expected answer: `kubectl logs <pod> --previous`, then `kubectl describe pod` for exit code and reason, then events.

---

**Q2. A pod is stuck `Pending`. Name the main causes and how you tell them apart.**

_Answer given:_ "1. Possible image issue, may not be available. 2. Resource like CPU, Memory issue. 3. Or the application/init container has somehow not come up yet."

_Score: 0.5_  
Insufficient resources is correct and is the most common cause. The other two were wrong, and both are diagnostic errors: an unavailable image gives `ImagePullBackOff`/`ErrImagePull`, and an init container that has not finished gives status `Init:0/1`. **Neither presents as `Pending`.** Pending means the scheduler has not placed the pod on a node at all, so nothing has been pulled and no container has started. Missing causes: no node satisfies taints/tolerations, node selectors or affinity rules; and an unbound PVC. Distinguished via `kubectl describe pod` and the scheduler's `FailedScheduling` event.

---

**Q3. A pod was `OOMKilled`. What happened, who killed it, what do you change?**

_Answer given:_ "Due to more memory usage than allocated. Some controller may have killed it, I don't know the name. I would change memory."

_Score: 0.5_  
Cause and remediation direction both correct. The killer was wrong and it is not a naming quibble: it is the **Linux kernel OOM killer**, acting on the container's cgroup when the process exceeds its memory limit. No Kubernetes component makes the decision; the kubelet only observes the exit and reports reason `OOMKilled`. Follow-up not reached: raise the limit only after checking whether the real cause is a leak, and the relationship between requests, limits and QoS class.

---

**Q4. A Service returns nothing and its endpoints list is empty. Why, and what do you check first?**

_Answer given:_ "IDK."

_Score: 0_  
Expected: the Service's label selector does not match any pod labels, or matching pods exist but are not Ready, so the endpoints controller excludes them. First checks: `kubectl get endpoints <svc>`, compare `spec.selector` against actual pod labels, then check pod readiness. Also relevant: `targetPort` pointing at the wrong container port.

---

**Q5. You need to see what just happened in a namespace, in order. Which command, and which flag makes it useful?**

_Answer given:_ "IDK."

_Score: 0_  
Expected: `kubectl get events --sort-by=.metadata.creationTimestamp` (or `.lastTimestamp`). Without the sort flag the output is unordered and effectively unusable. Also worth knowing: events expire, default retention is about one hour.

---

**Q6. A container hits its CPU limit; another hits its memory limit. Two different outcomes. What and why?**

_Answer given:_ "Memory hit is OOM issue, other IDK."

_Score: 0.5_  
Memory half correct. CPU not answered. Expected: **a CPU limit throttles, it never kills.** The kernel's CFS quota simply gives the container fewer cycles per period, so the application becomes slow while showing no restarts and no OOM events. A memory limit, by contrast, is enforced by killing. This asymmetry is why CPU-limit problems are much harder to detect than memory-limit ones, and it is a common senior-level follow-up.

---

**Q7. A liveness probe is too aggressive and the app is under heavy load. What goes wrong?**

_Answer given:_ "The pod takes time to come up and the app is not responding by that time. Liveliness says application should be ready but actually it is not ready."

_Score: 0.5_  
The intuition about slow response under load is right, but the answer describes **readiness**, not liveness, and conflating the two is itself a gap. Liveness failing does not mark the pod unready; **the kubelet restarts the container.** Under load this produces a cascading failure: a healthy-but-slow pod is killed, its traffic shifts to the remaining pods, those become slower, their probes now fail too, and the restarts spread. Related concepts not reached: `initialDelaySeconds`, startup probes for slow-starting apps, and why liveness probes should be cheap and independent of downstream dependencies.

---

**Q8. A rollout has gone bad. Commands to check status, see history, and roll back?**

_Answer given:_ "IDK."

_Score: 0_  
Expected: `kubectl rollout status deployment/<name>`, `kubectl rollout history deployment/<name>`, `kubectl rollout undo deployment/<name>` (optionally `--to-revision=N`). Also relevant: `maxSurge`/`maxUnavailable`, and why a rollout can hang forever when new pods never become ready.

---

**Q9. ConfigMap as env vars vs mounted as a volume. What difference matters in production?**

_Answer given:_ "IDK."

_Score: 0_  
Expected: **env vars are captured at container start and never change**, so a ConfigMap update requires a pod restart to take effect. A mounted volume is updated in place by the kubelet within a sync period (roughly a minute), so an app that re-reads the file can pick up changes without a restart. Secondary: subPath mounts break the auto-update behaviour; env vars leak into `kubectl describe` and crash dumps.

---

**Q10. A pod cannot resolve `my-service`. Trace the DNS path end to end.**

_Answer given:_ "IDK."

_Score: 0_  
Expected chain: the pod's `/etc/resolv.conf` (written by the kubelet, with the cluster DNS ClusterIP as nameserver and a `search` list including `<ns>.svc.cluster.local`) → the short name is expanded through the search domains → the query reaches the CoreDNS Service ClusterIP → kube-proxy rules route it to a CoreDNS pod → CoreDNS answers from its Kubernetes plugin with the Service's ClusterIP → the pod connects to that ClusterIP → kube-proxy's iptables or IPVS rules DNAT the connection to a real backing pod IP. Common failure points: wrong namespace, CoreDNS pods down, NetworkPolicy blocking port 53, `dnsPolicy` misconfiguration.

---

## Summary

|Q|Topic|Score|
|---|---|---|
|1|CrashLoopBackOff, `logs --previous`|0.5|
|2|Pending causes|0.5|
|3|OOMKilled|0.5|
|4|Service with empty endpoints|0|
|5|Ordered namespace events|0|
|6|CPU throttle vs memory kill|0.5|
|7|Aggressive liveness probe|0.5|
|8|Rollout status / history / undo|0|
|9|ConfigMap env vs volume|0|
|10|Cluster DNS resolution path|0|
||**Total**|**2.5 / 10**|

# Kubernetes Self-Audit — Pass 2 (Architecture)

Same conditions. Cold, no cluster, no notes, no AI.

---

**A1. What happens after `kubectl apply -f deployment.yaml`?**

_Answer:_ "The deployment gets applied and if replicas are there then replicaset is created and then the pod is started. I think some manager manages this and etcd stores the state and till desired state = achieved state Kubernetes tries to achieve it."

_Score: 1.0_

Correct, and the best answer of the whole audit. The Deployment → ReplicaSet → Pod chain is right, etcd as the store is right, and reconciliation toward desired state is right and is the single most important idea in Kubernetes. "Some manager" is the controller manager, and the scheduler and kubelet are missing from the chain, but the mechanism you described is genuinely correct.

Full chain: kubectl sends the manifest to the **API server** → API server authenticates, authorizes, validates, writes to **etcd** → the **deployment controller** (in the controller manager) sees a Deployment with no matching ReplicaSet, creates one → the **replicaset controller** sees a ReplicaSet with 0 of N pods, creates Pod objects with no node assigned → the **scheduler** watches for unscheduled pods, picks a node, writes the binding → the **kubelet** on that node sees a pod assigned to it, calls the container runtime, pulls the image, starts the container, reports status back → status lands in etcd, and the loop keeps running forever.

_Note: your plan calls this "the single highest-value item" on Checklist C. You are partway there already._

---

**A2. Deployment vs StatefulSet vs DaemonSet.**

_Answer:_ "IDK."

_Score: 0_

Expected: **Deployment** for stateless, interchangeable replicas, random pod names, any pod can replace any other. **StatefulSet** for workloads needing stable identity: ordered names (`db-0`, `db-1`), a stable DNS name per pod, its own persistent volume that follows it across restarts, and ordered startup and shutdown. Databases, Kafka, etcd. **DaemonSet** for one pod per node, used by log collectors, monitoring agents and CNI plugins. Missing from the list and worth knowing: Job and CronJob.

---

**A3. Requests vs limits, and which does the scheduler use?**

_Answer:_ "Requests is how much is really required and limit is under load max how much it can go."

_Score: 0.5_

The plain-English meaning is right. What is missing is the part that matters operationally: **the scheduler only looks at requests.** It sums the requests of all pods on a node and places a new pod only where the requests fit. Limits are invisible to the scheduler and are enforced at runtime by the kernel, CPU by throttling and memory by killing, as in Q6 of pass 1.

That gap explains a very common production incident: a node where every pod is well within its requests but the node is overcommitted on limits, so pods throttle or get OOMKilled while the cluster reports plenty of free capacity.

Also unasked: requests and limits together determine **QoS class** (Guaranteed, Burstable, BestEffort), which decides eviction order under node pressure.

---

**A4. What makes ClusterIP traffic reach a pod?**

_Answer:_ "IDK."

_Score: 0_

Expected: **kube-proxy**, running on every node. It watches Services and endpoints through the API server and programs the node's iptables or IPVS rules. A ClusterIP is a virtual IP that exists nowhere as an interface; nothing listens on it. When a pod sends traffic there, the kernel's netfilter rules rewrite the destination to a real pod IP, chosen roughly at random from the ready endpoints. That is why an empty endpoints list means silence rather than an error, which links straight back to Q4 of pass 1.

---

**A5. What does an app in a pod need to call the Kubernetes API?**

_Answer:_ "IDK."

_Score: 0_

Expected: a **ServiceAccount**, whose token the kubelet mounts into the pod, plus **RBAC** permissions granted to that ServiceAccount through a Role or ClusterRole bound by a RoleBinding or ClusterRoleBinding. Without a binding, the default ServiceAccount can do essentially nothing. This is the mechanism every controller and operator runs on, including the CDP controller you work alongside.

---

## Pass 2 summary

|Q|Topic|Score|
|---|---|---|
|A1|Post-`kubectl apply` reconciliation|1.0|
|A2|Deployment / StatefulSet / DaemonSet|0|
|A3|Requests vs limits|0.5|
|A4|ClusterIP and kube-proxy|0|
|A5|ServiceAccount and RBAC|0|
||**Pass 2 total**|**1.5 / 5**|

**Combined: 4.0 / 15 (27%).**

---

