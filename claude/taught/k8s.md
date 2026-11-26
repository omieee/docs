# Kubernetes: taught list (Claude; check before any K question or lesson)

Only what Om has watched or been taught, with the date. Anything not here is not tested. Created Nov 20 2026 after the K1 untaught-questions error.

## K1 (KodeKloud CKA, Core Concepts, introduction lessons)
- Watched: Cluster Architecture, Docker-vs-ContainerD, A Note on Docker Deprecation (Nov 17); etcd for Beginners, etcd in Kubernetes, Kube API Server, Kube Controller Manager, Kube Scheduler, Kubelet, Kube Proxy (Nov 18). Also watched, ahead and not tested in K1: etcd Commands (optional), Pods, Pods with YAML, Demo: Pods with YAML.
- Level: introductions of what each component is (Om, Nov 20). Om's own kind notes (docs `k8s/k8s-notes.md`, PR #3, Nov 19): what each of the six does, which are control plane Pods on kind, kube-proxy a Pod, kubelet a systemd process inside the kind node container.
- Taught by Claude in chat (not the course): Nov 13, the scheduler picks a node and writes it into the Pod, the kubelet starts the containers; Nov 19, kube-proxy handles Service traffic to Pods; kubelet must run before any Pod exists.
- Earlier: kind cluster and a first pod, `port-forward` (Oct 26, ChatGPT). Om's IBM use: `describe`, `logs`, events often; `apply`, `port-forward`, `kubectl run` less (Nov 13).

## K2 (KodeKloud CKA, Core Concepts, workload lessons, course order)
- Watched: ReplicaSets (16:09), Nov 22 at bedside (Om 22:48). Done before Nov 25 (KodeKloud ticks, screenshot Nov 25 18:06): Practice Test Introduction, Lab: Pods, Lab Solution: Pods. Done Nov 25: Lab: ReplicaSets (all right, Om Nov 26). Done Nov 26: Deployments (04:21) video, Certification Tip!, Lab: Deployments (all right; last question typed `alipine` for `alpine`, Om's words). Lab Solution: Deployment (optional) not done. Not yet: Services onward.
- Taught in chat: a ReplicaSet keeps the desired count, scaling is changing `replicas`, the scheduler (not the ReplicaSet) picks the node (Nov 22); the selector picks the Pods a ReplicaSet counts, by their labels, including matching Pods made before it (Om's own answer Nov 25, confirmed). Nov 26: a Deployment works through a ReplicaSet, never on Pods directly (Deployment, then ReplicaSet, then Pods); one Deployment has one Pod template and all its Pods are identical copies, so a frontend and a backend are two Deployments (counterexample: what would `replicas: 3` mean with two templates).

## Not taught yet (do not test)
- The Pod start sequence step by step: K2's "full chain after `kubectl apply`" (W11).
- Failure symptoms and checks (Pending, events for scheduling): K2's ten scenarios.
- Component counts on multi-node clusters.
