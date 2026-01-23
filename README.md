## Steps

1. Create frontend, backend apps, ran locally

2. Set up Dockerfile for frontend, backend; Add docker-compose.yml

3. git commit & push to GitHub

4. Launch EC2 instance with Ubuntu 24.04, t3.micro, SSH from 0.0.0.0, stored ssh key file

5. ssh into the instance using the key file

6. Set up the server using commands:

```bash
sudo apt update && sudo apt upgrade -y # Update & upgrade packages

sudo apt install git -y # Install git
git --version # Check git version

# Install dependencies & Add Docker's official GPG key
sudo apt install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Add the repository to Apt sources
sudo tee /etc/apt/sources.list.d/docker.sources <<EOF
Types: deb
URIs: https://download.docker.com/linux/ubuntu
Suites: $(. /etc/os-release && echo "${UBUNTU_CODENAME:-$VERSION_CODENAME}")
Components: stable
Signed-By: /etc/apt/keyrings/docker.asc
EOF
sudo apt update

# Install docker & docker compose
sudo apt install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

# Check
docker --version
docker compose version
sudo systemctl status docker
sudo systemctl start docker # If status = not running

# Run docker without sudo (add user to docker user group)
sudo usermod -aG docker $USER

sudo reboot # For all changes to take effect
```

Then ssh again and enter docker ps to check if user was added to docker group

7. Clone GitHub repository:

```bash
git clone "https://github.com/rajsekharde/ec2-pipeline-test.git"
cd ec2-pipeline-test
```

8. Build and run the containers:

```bash
docker compose up --build -d
```

9. Access traefik & prometheus dashboards using ssh port forwarding:

```bash
ssh -i "<key-pair file>" -L 8080:localhost:8080 -L 9090:localhost:9090 ubuntu@<Public IPv4 address of EC2 instance>
```