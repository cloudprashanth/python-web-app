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
docker build -t python-docker-app .
```
Push the image to your favourite repository
