# Create the K8s cluster

## How to deploy
- Create the K8s cluster
```bash
❯ task create-k8s-cluster
task: [create-k8s-cluster] kind create cluster --config=config.yaml
Creating cluster "github-arc-poc" ...
 ✓ Ensuring node image (kindest/node:v1.33.1) 🖼
 ✓ Preparing nodes 📦 📦 📦
 ✓ Writing configuration 📜
 ✓ Starting control-plane 🕹
 ✓ Installing CNI 🔌
 ✓ Installing StorageClass 💾
 ✓ Joining worker nodes 🚜
Set kubectl context to "kind-github-arc-poc"
You can now use your cluster with:

kubectl cluster-info --context kind-github-arc-poc

Thanks for using kind! 😊
```

- Check the K8s cluster is avalilable
```bash
❯ task check-k8s-cluster-is-avalilable
task: [check-k8s-cluster-is-avalilable] kind get clusters
github-arc-poc
task: [check-k8s-cluster-is-avalilable] kubectl get nodes
NAME                           STATUS   ROLES           AGE    VERSION
github-arc-poc-control-plane   Ready    control-plane   2m5s   v1.33.1
github-arc-poc-worker          Ready    <none>          106s   v1.33.1
github-arc-poc-worker2         Ready    <none>          105s   v1.33.1
```

## How to undeploy
- Delete the K8s cluster
```bash
❯ task delete-k8s-cluster
task: [delete-k8s-cluster] kind delete cluster --name "github-arc-poc"
Deleting cluster "github-arc-poc" ...
Deleted nodes: ["github-arc-poc-control-plane" "github-arc-poc-worker2" "github-arc-poc-worker"]
```
