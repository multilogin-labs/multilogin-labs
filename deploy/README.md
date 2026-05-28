# deploy · infrastructure templates

| Path | What |
|---|---|
| [helm/multilogin-labs](helm/multilogin-labs/) | Helm chart: warmup CronJob + optional Pages mirror |
| [terraform/](terraform/) | Terraform: S3 bucket + website config (Pages mirror to a custom domain) |

## Helm

```bash
kubectl create secret generic multilogin-secrets \
  --from-literal=MULTILOGIN_TOKEN=... \
  --from-literal=MULTILOGIN_FOLDER_ID=... \
  --from-literal=MULTILOGIN_LAUNCHER=https://launcher.example.com:45001

helm install mlx deploy/helm/multilogin-labs \
  --set warmup.envFromSecret=multilogin-secrets
```

## Terraform

```bash
cd deploy/terraform
terraform init
terraform plan
terraform apply
```

> These are minimal scaffolds. Adapt to your cluster / cloud setup. PRs welcome.
