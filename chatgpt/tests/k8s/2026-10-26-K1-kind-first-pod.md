# K1 Part 1 · 2026-10-26 · W4 · kind cluster and first Pod

Owner: ChatGPT. Planned box: W4 K1 1.5h (90m), Om permitted 120m; actual focused learner minutes **~60m ESTIMATED BY OM**, not measured; Om said "Time i didnot calculate may be an hour or so .. but ok i still may have 30-45 min time". Do not infer precision from timestamps. No final K1 verdict: full unit includes W5–W7 kubectl surfaces and the 10-task cold drill (8/10). Terminal evidence below is Om's pasted output; ChatGPT did not run commands itself.

## Prerequisite and learning evidence

- Om baseline: Docker 1–2 commands years ago, kind never used, kubectl used with icdctl at IBM for cluster/Pod/describe. Docker runtime confirmed by `docker run --rm hello-world` ("Hello from Docker!"); kind and kubectl are installed.
- Om provided KodeKloud screenshot showing `Pods` (9:04), `Pods With YAML` (6:44), `Demo - Pods With YAML` (6:17), `Practice Test Introduction` (5:45), and `Lab - Pods` marked completed. Screenshot does not expose lab answers.
- Resource-selection coach error separately recorded in `chatgpt-log-entries.md` on Oct 26 11:19 IST (31-second intro incorrectly offered as learning resource). Correction supplied.
- W4 scope: kind cluster up and first Pod; no K2 deep architecture.

## Om terminal proof (excerpts, verbatim)

```console
> kind get clusters
No kind clusters found.

> kind create cluster --name phase1-k1
Creating cluster "phase1-k1" ...
 ✓ Ensuring node image (kindest/node:v1.37.0) 🖼️
 ✓ Preparing nodes 📦  
 ✓ Writing configuration 📜 
 ✓ Starting control-plane 🕹️ 
 ✓ Installing CNI 🔌 
 ✓ Installing StorageClass 💾 
Set kubectl context to "kind-phase1-k1"
You can now use your cluster with:

kubectl cluster-info --context kind-phase1-k1

Thanks for using kind! 😊

> kubectl config current-context
kind-phase1-k1

> kubectl get nodes             
NAME                      STATUS   ROLES           AGE     VERSION
phase1-k1-control-plane   Ready    control-plane   2m43s   v1.37.0

> kubectl run k1-nginx --image=nginx:stable-alpine
pod/k1-nginx created

> kubectl get pods                                
NAME       READY   STATUS    RESTARTS   AGE
k1-nginx   1/1     Running   0          2m40s
```

Full `kubectl describe pod k1-nginx` pasted in chat: namespace `default`, node `phase1-k1-control-plane/172.18.0.2`, Pod IP `10.244.0.5`, image `nginx:stable-alpine`, image digest `sha256:47928bf67eb62a1863cb08d9ecb52d3e704304ba614eaee17884204677702951`, `State: Running`, `Ready: True`, `Restart Count: 0`. Events, in order: Scheduled -> Pulling -> Pulled (12.259s) -> Created -> Started. No probe or end-to-end HTTP check yet at this point.

```console
> kubectl port-forward pod/k1-nginx 8080:80
Forwarding from 127.0.0.1:8080 -> 80
Forwarding from [::1]:8080 -> 80

> curl -i http://127.0.0.1:8080
HTTP/1.1 200 OK
Server: nginx/1.30.6
Date: Mon, 26 Oct 2026 08:46:12 GMT
Content-Type: text/html
Content-Length: 896
...
<h1>Welcome to nginx!</h1>
...
```

After Om stopped port-forward:

```console
> curl -i http://127.0.0.1:8080
curl: (7) Failed to connect to 127.0.0.1 port 8080 after 0 ms: Couldn't connect to server
```

Then independent status check after tunnel stopped:

```console
> kubectl get pods                         
NAME       READY   STATUS    RESTARTS   AGE
k1-nginx   1/1     Running   0          23m
```

## Concept checks (Om's answers verbatim, first attempt preserved)

**Q1 original**: "Why is `pod/k1-nginx created` alone insufficient proof that the container actually started? Use the evidence from your `describe` output."

Om: "It may be the pod came up but is it accessible to outside world that is not proven"

First score PARTIAL 1/2: he distinguished public accessibility, but that was not the container-start proof asked for. Taught created vs started vs accessible, with missing image counterexample.

**Q1 fresh retry**: "Suppose this command reports `pod/test created`: `kubectl run test --image=nginx:nonexistent-tag-123`. Can we conclude the container started? What evidence would you check to confirm?"

Om (verbatim):
> So in this non existanct case lot of things will be different :
>
> 1. kubectl get pod will give 0/1 in ready and status ass ErrImagePull&#x20;
> 2. also describing the pod in Containers dictionany State will be stuck at waiting and Ready will be False

Retry scored 2/2; original miss retained.

**Q2 original**: "Suppose you press `Ctrl+C` in the terminal running `kubectl port-forward`, then run the same `curl` command again. What happens to the HTTP request, and what happens to the nginx Pod? Why?"

Om: "Error should come most probaby 404 or host not exist"

First score PARTIAL 0.5/2: request failure predicted, but 404 and DNS failure incorrect, and Pod not addressed. Taught local listener removed vs HTTP 404, with curl exit code 7.

**Q2 fresh retry**: "Will `k1-nginx` still show `Running`? Explain why `curl` can fail even though the Pod is healthy."

Om: "pods will be there we are stoping port forward we are not kiiling the application"

Retry scored 2/2. Confirmed empirically by curl failure + still-running Pod. Original miss retained.

## Status at save

- W4 practical milestone **EVIDENCED**, using Om's pasted terminal proof, not an assistant-run terminal or GitHub CI.
- Demonstrated cluster creation, correct context, Ready node, first nginx Pod running, `describe` event chain, port-forward and HTTP 200, independent Pod survival after tunnel stop.
- Current concept repairs landed on fresh retries; original two misses remain in this record.
- Not yet K1 unit close: remaining `kubectl` surfaces in W5–W7; no three-question unit cold proof or scheduled 10-task drill yet.
- Active duration: [~60m] Om's approximate self-report, not measured. Up to ~30m of original W4 90m K1 box remains for independent practice, not added unit scope. No auto-inferred clock duration, no exact pace claim. No public exposure or Service/Ingress tested.


## 30-minute optional W4 interview, Round 1 (user asked for rigorous assessment including Pod YAML)

**Question as asked:**
"Create `k1-interview.yaml`, a standalone Pod named `k1-interview` in namespace `default`, exactly one container `web`, image `nginx:stable-alpine`, label `app: k1-interview`. No AI/copy/docs for first attempt. Paste complete YAML before applying."

**Om's first answer, verbatim:**

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: k1-interview
  label:
    app: k1-interview
spec:
  containers:
  - name: k1-interview
    image: nginx:stable-alpine
```

**Om's spontaneous revision, verbatim, before coach scoring:**

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: k1-interview
  label:
    app: k1-interview
spec:
  containers:
  - name: web
    image: nginx:stable-alpine
```

**Round 1 first score:** 4/7 rubric points (Pod/v1 yes, Pod name yes, explicit namespace no, exactly one container yes, container name no, image yes, correct label no). Revision now 5/7 (container name corrected unprompted). Unverified: actual file path and runtime validity, because only pasted content was seen. The omitted namespace could resolve to `default` under current kubectl context, but is not an explicit manifest guarantee. `metadata.label` (singular) is unrecognised; use `metadata.labels`. Keep original answer and score as recorded, even after correction. No full unit verdict. Continued repair prompt: correct both metadata fields in own YAML, paste, then run proof.


**Om's post-feedback corrected YAML, verbatim:**

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: k1-interview
  namespace: default
  labels:
    app: k1-interview
spec:
  containers:
  - name: web
    image: nginx:stable-alpine
```

**Round 1 repair assessment:** 7/7 of the specified fields present and structurally correct on textual review. This is a successful coached repair, not a retroactive 7/7 cold first attempt; first attempt remains 4/7 and spontaneous pre-feedback revision 5/7. No cluster execution proof yet. Next: save as `k1-interview.yaml` and execute `kubectl apply --context kind-phase1-k1 -f k1-interview.yaml` and paste output; then inspect the Pod.

**Round 2 first runtime evidence, Om's terminal output, verbatim:**

```console
> kubectl apply --context kind-phase1-k1 -f k1-interview.yaml 
pod/k1-interview created
```

Result: manifest accepted by API server, object created. Container running/state and name/node verification NOT YET CHECKED. Interview prompt next (no command supplied): "Show that `k1-interview` is running, identify the node it runs on, and confirm its container is named `web`. Use the kubectl commands you have already learned. Paste your commands and terminal output."


### Round 2 independent verification

**Prompt as asked:** "Show that `k1-interview` is running, identify the node it runs on, and confirm its container is named `web`. Use the `kubectl` commands you have already learned. Paste your commands and terminal output."

**Om's answer, verbatim (selected commands and full information required for proof):**

```text
Containers:
  web:

kubectl get pods -owide
NAME           READY   STATUS    RESTARTS   AGE    IP           NODE                      NOMINATED NODE   READINESS GATES
k1-interview   1/1     Running   0          50s    10.244.0.7   phase1-k1-control-plane   <none>           <none>
k1-nginx       1/1     Running   0          128m   10.244.0.5   phase1-k1-control-plane   <none>           <none>

> kubectl describe pod k1-interview 
Name:             k1-interview
Namespace:        default
Priority:         0
Service Account:  default
Node:             phase1-k1-control-plane/172.18.0.2
Start Time:       Mon, 26 Oct 2026 16:04:29 +0530
Labels:           app=k1-interview
Annotations:      <none>
Status:           Running
IP:               10.244.0.7
IPs:
  IP:  10.244.0.7
Containers:
  web:
    Container ID:   containerd://c6f8aaf3b5ce6de54fcf2008ec717f460f534a02bd771b2e84492d4c29aac462
    Image:          nginx:stable-alpine
    Image ID:       docker.io/library/nginx@sha256:47928bf67eb62a1863cb08d9ecb52d3e704304ba614eaee17884204677702951
    Port:           <none>
    Host Port:      <none>
    State:          Running
      Started:      Mon, 26 Oct 2026 16:04:30 +0530
    Ready:          True
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-bbzvp (ro)
Conditions:
  Type                        Status
  PodReadyToStartContainers   True 
  Initialized                 True 
  Ready                       True 
  ContainersReady             True 
  PodScheduled                True 
Volumes:
  kube-api-access-bbzvp:
    Type:                    Projected (a volume that contains injected data from multiple sources)
    TokenExpirationSeconds:  3607
    ConfigMapName:           kube-root-ca.crt
    Optional:                false
    DownwardAPI:             true
QoS Class:                   BestEffort
Node-Selectors:              <none>
Tolerations:                 node.kubernetes.io/not-ready:NoExecute op=Exists for 300s
                             node.kubernetes.io/unreachable:NoExecute op=Exists for 300s
Events:
  Type    Reason     Age   From               Message
  ----    ------     ----  ----               -------
  Normal  Scheduled  77s   default-scheduler  Successfully assigned default/k1-interview to phase1-k1-control-plane
  Normal  Pulled     76s   kubelet            spec.containers{web}: Container image "nginx:stable-alpine" already present on machine and can be accessed by the pod
  Normal  Created    76s   kubelet            spec.containers{web}: Container created
  Normal  Started    76s   kubelet            spec.containers{web}: Container started
```

**Score:** PASS 3/3: commands independently selected; Pod Running/1-of-1 Ready, correct node and container `web` established by independent CLI evidence. Same node/image digest as `k1-nginx`; no fresh pull needed because image already present. The container readiness result is not a substitute for independent HTTP test. Final interview cold questions remain pending; do not close entire K1 unit.


### Round 3 cold Q1: manifest-to-container mechanism

**Prompt as asked:** "You applied `k1-interview.yaml`, and a few seconds later the Pod was `Running`. Explain the sequence from submitting the YAML to the container starting. Include which Kubernetes component chose the node and which component started the container."

**Om's first cold answer, verbatim:**

> when i placed the order first scheduler schedules it and maps to teh node phase1-k1-control-plane then kublet will go to fetch the image if retrivable that is pulled by kublet and the kublet will create the container and finally kublet will report as started

**First-attempt score: PARTIAL 3/4.** Correct scheduler node assignment, kubelet role, and status reporting. Missed that API server validates and records the Pod before scheduling. Clarification: image pull and container create/start are done by the container runtime under kubelet's direction. Prior minimal API-server sequence was taught in conversation; this is not an untaught K2 internals quiz. Explained the smallest chain and counterexample (invalid YAML is rejected by API server; no Pod exists for scheduler to place). One fresh retry pending; original score remains on record.


### Round 3 Q1 retry and cold Q2

**Retry prompt as asked:** "Suppose you submit a Pod YAML file containing an invalid Kubernetes field. Would the scheduler attempt to assign that Pod to a node? Explain which component handles the request first and why scheduling would or would not happen."

**Om's retry answer, verbatim:**

> Scheduler will not get the pod yaml file because it will be rejected by api server only

**Retry score: PASS 2/2.** Correct rejection by API server prevents scheduling. Precision note from coach: scheduler watches accepted, unscheduled Pod objects, not local YAML files. Original score 3/4 remains.

**Cold Q2 as asked:**

> You create another Pod using a valid YAML file. Its status becomes: `test-pod 0/1 ImagePullBackOff 0`. The Kubernetes node is `Ready`.
>
> Without notes or AI, explain:
> 1. What does `ImagePullBackOff` tell you?
> 2. Which `kubectl` command would you run first to investigate, and what evidence would you look for?
> 3. Would `kubectl port-forward` fix this problem? Why or why not?
>
> Answer all three. I'll score them together before Question 3.

**Answer:** pending.

### Round 3 Q2: ImagePullBackOff troubleshooting

**Om's first cold answer, verbatim:**

> 1. that the kublet was not able to pull the image mentioned in the yaml either image is not there or auth error while pulliungh
> 2. kubectl describe pod test-pod and will look for events related to Image pulls
> 3. No port forward works after pod is reeady to serve users it just exposes the port to be used via different port from outside it doesnot fix the pod issue or bad image of the container

**First score: PARTIAL 2.5/3.** 1/1 image pull error causes; 1/1 `kubectl describe pod test-pod` and Events; 0.5/1 correctly excludes port-forward as image pull fix, but incorrectly says Pod must be Ready and suggests external reachability. Taught: `ImagePullBackOff` incorporates delays between retries; `kubectl port-forward` waits for a Running Pod, does not require a Ready condition, and binds localhost by default (not public exposure). Official kubectl reference confirmed `--pod-running-timeout` and default `--address localhost`: https://kubernetes.io/docs/reference/kubectl/generated/kubectl_port-forward/. Fresh transfer check pending. Original score remains on record; no unit verdict.
