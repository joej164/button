# button

# Deploying as a service on Raspberry Pi Ubuntu 20.04

## Assumptions

- Code installed at `/home/ubuntu/repos/button`

## Instructions

1. Copy the `service/docker-compose-button.service` to /etc/systemd/system
2. Restart systemctl `sudo systemctl daemon-reload`
3. Start the service `sudo systemctl start docker-compose-button`
4. Set the service to start on boot `sudo systemctl enable docker-compose-button`

# Seeing what's going on with the service

- `docker ps`
- Systemctl commands
  - `systemctl status docker-compose-button`
  - `sudo systemctl restart docker-compose-button`
  - `sudo systemctl start docker-compose-button`
  - `sudo systemctl stop docker-compose-button`
