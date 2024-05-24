# Create the K8s cluster

## How to deploy
- Check deployment prerequisites
```bash
❯ cd kind

❯ source .envrc

❯ docker version
Client: Docker Engine - Community
 Version:           26.0.1
 API version:       1.45
 Go version:        go1.21.9
 Git commit:        d260a54
 Built:             Thu Apr 11 10:54:59 2024
 OS/Arch:           linux/amd64
 Context:           default

Server: Docker Engine - Community
 Engine:
  Version:          26.0.1
  API version:      1.45 (minimum version 1.24)
  Go version:       go1.21.9
  Git commit:       60b9add
  Built:            Thu Apr 11 10:53:19 2024
  OS/Arch:          linux/amd64
  Experimental:     false
 containerd:
  Version:          1.6.31
  GitCommit:        e377cd56a71523140ca6ae87e30244719194a521
 runc:
  Version:          1.1.12
  GitCommit:        v1.1.12-0-g51d5e94
 docker-init:
  Version:          0.19.0
  GitCommit:        de40ad0

❯ kind version
kind v0.20.0 go1.20.4 linux/amd64
```

- Create the K8s cluster
```bash
❯ kind create cluster --config=config.yaml
Creating cluster "github-arc-poc" ...
 ✓ Ensuring node image (kindest/node:v1.27.3) 🖼
 ✓ Preparing nodes 📦 📦 📦
 ✓ Writing configuration 📜
 ✓ Starting control-plane 🕹️
 ✓ Installing CNI 🔌
 ✓ Installing StorageClass 💾
 ✓ Joining worker nodes 🚜
Set kubectl context to "kind-github-arc-poc"
You can now use your cluster with:

kubectl cluster-info --context kind-github-arc-poc

Have a question, bug, or feature request? Let us know! https://kind.sigs.k8s.io/#community 🙂
```

- Check the K8s cluster is created
```bash
❯ kind get clusters
github-arc-poc

❯ kubectl get nodes
NAME                           STATUS   ROLES           AGE   VERSION
github-arc-poc-control-plane   Ready    control-plane   78s   v1.27.3
github-arc-poc-worker          Ready    <none>          56s   v1.27.3
github-arc-poc-worker2         Ready    <none>          54s   v1.27.3
```

## How to undeploy
- Delete the K8s cluster
```bash
❯ kind delete cluster --name github-arc-poc
Deleting cluster "github-arc-poc" ...
Deleted nodes: ["github-arc-poc-control-plane" "github-arc-poc-worker" "github-arc-poc-worker2"]

❯ kind get clusters
No kind clusters found.
```
