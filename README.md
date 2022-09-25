# Python Web App

This is a basic Hello world Web App using python

Major tools used for the App.
- Python
- Flask
- Docker
- Kubernetes
- Helm

In your machine(I'm using Amazon Linux2), make sure you have them installed
## Installations

### Python installation:
```sh
sudo yum install python34 python34-pip
```

### Docker installation:
```sh
sudo yum install docker
sudo usermod -a -G docker ec2-user (This command is used to add ec2 user into docker group)
```

### Kubectl installation:
```sh
curl -o kubectl https://s3.us-west-2.amazonaws.com/amazon-eks/1.23.7/2022-06-29/bin/linux/amd64/kubectl
chmod +x ./kubectl
mkdir -p $HOME/bin && cp ./kubectl $HOME/bin/kubectl && export PATH=$PATH:$HOME/bin
```

### Helm installation:
```sh
curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3
chmod 700 get_helm.sh
./get_helm.sh
```
Folder Tree
```sh
├── app.py
├── Dockerfile
└── requirements.txt
```
### Creating Docker image
The following command is used to create docker image
```sh
docker build -t itzprashanth/python-docker-app:latest .
```
Push the image to your favourite repository
```sh
docker push itzprashanth/python-docker-app:latest
```
Create a helm chart using following command
```sh
helm create python-docker-app
```
Updates made on helm charts
- Update python-web-app/templates/deployment.yaml file, I updated containerPort to 5000
- Update python-web-app/values.yaml file with required details, in my case I updated image repository, tag of docker image to latest, autoscaling values and service type to LoadBalancer
```sh
autoscaling:
  enabled: true
  minReplicas: 1
  maxReplicas: 5
  targetCPUUtilizationPercentage: 40
```
- To dry run the helm chart, run the following command
```sh
helm install --dry-run ./python-web-app/ --generate-name
```
- To run the helm chart
```sh
helm install ./python-web-app/ --generate-name
```
- To list the helm charts installed
```sh
helm list
```
- To list the running pods
```sh
kubectl get pods
```
- If you found any errors in the running pods, run the following command to get the details of the pods
```sh
kubectl describe pod python-web-app-1664126080-6bfcdcfdfc-vskk9
```
- To delete the helm chart, run the following command
```sh
helm uninstall python-web-app-1664126080
```
## Result
### Access the website from www.prashanthg.tk
### Routes
### www.prashanthg.tk/app
### www.prashanthg.tk/time
