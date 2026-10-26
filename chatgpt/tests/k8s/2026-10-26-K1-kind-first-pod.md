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
