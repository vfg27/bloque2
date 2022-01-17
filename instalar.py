#Marta Morán, Miguel Varas y Victor Fresno
import sys
import json
import time
from subprocess import call
call(["echo 'y' | sudo apt-get update"], shell=True)
call(["sudo apt-get install \
    ca-certificates \
    curl \
    gnupg \
    lsb-release"], shell=True)
call(["curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg"], shell=True)
call(["echo \
  'deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable' | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null"], shell=True)
call(["echo 'y' | sudo apt-get update"], shell=True)
call(["sudo apt-get install docker-ce docker-ce-cli containerd.io"], shell=True)
call(["sudo docker run hello-world"], shell=True)
