# Task 1 - Setting up the app in an Ubuntu VM
## VM Installation
Download the latest version of Virtual Box and Ubuntu from their websites

Set up VirtualBox and run it

    VirtualBox -> https://www.virtualbox.org/wiki/Downloads

Create a new environment by using default allocations

Boot up the new environment and use the Ubuntu ISO file to install the OS

Clone this repo in your VM. The Ansible directory is unused for this portion.

    git clone https://github.com/Todaku/DockerAnsibleCounter.git

## Docker Installation (from Docker documentation)
- Setting up Docker repository
  update apt

      sudo apt-get update

  allow apt over https

      sudo apt-get install \
      apt-transport-https \
      ca-certificates \
      curl \
      software-properties-common

  Get Docker GPG key

      curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

  Verify key was added

      sudo apt-key fingerprint 0EBFCD88

  Output should give the following key fingerprint

      9DC8 5822 9FC7 DD38 854A E2D8 8D81 803C 0EBF CD88

  Setup stable repository

      sudo add-apt-repository \
      "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
      $(lsb_release -cs) \
      stable"

- Install docker

  Install the package

      sudo apt-get install docker-ce

  Verify success by using docker to run the default hello-world docker repo

      sudo docker run hello-world

  ** remember to use sudo before calling Docker

## Setting up things for the Web App

- Libraries needed:

    pip, Flask, redis, docker-compose

      sudo apt install python-pip
      sudo pip install Flask
      sudo pip install redis
      sudo pip install docker-compose

- Brief explanation of usage

      pip -> install python related packages
      Flask -> Framework for python webapps
      redis -> Networking capabilities for python webapps (ie Tracking the counter)
      docker-compose -> Automate running the Docker containers

- Running everything

    Clone the repo; then make the call to docker-compose to run all the docker files

      sudo docker-compose up

    Head over to browser and bring up localhost:5000. Refreshing this page will increment the counter by 1
    whereas going to localhost:5001 will reset the counter such that visiting localhost:5000 will show a counter
    reset to a value of 1.

    Close the hosts with a ctrl+c keyboard input

# Task 2 - Automate the app using Ansible
## Automating the Process with Ansible
- Libraries needed:

    Vagrant, Ansible

    Vagrant setup -> https://www.vagrantup.com/downloads.html

- Setting things up

    Navigate to the /ansible/ directory and set up vagrant

      vagrant up

    This is needed initialize vagrant

    ** Needs to install an ubuntu box image (may take some time)

    The Ansible playbook will do all of the following:

      Copy the needed files
      Install Docker
      Install Docker-compose
      Run Docker-compose^1
    ^1: This step will not terminate the play book running, so we need to open up another terminal and ssh into the
    vm to see the results

    Verify Docker is installed correctly by sshing into the Vagrant Box

      vagrant ssh
      sudo docker run hello-world

    Correct output will the be hello-world message from Docker

    Before we check the output, it'll take about a minute or two in order for docker
    to come up, if connection is refused just try again in a minute

    Move into the /pythonapp/ directory do the following:

      curl localhost:5000
      The following will appear:
        Counter: X; refreshing this page increments by 1; going to :5001 container will reset (:5000)
      Using the other container:
        curl localhost:5001
        This is the 2nd container under the /sub directory; upon access, the counter will reset to 0. (:5001)

    Success!

# Concluding remarks

  Overall the task was a great learning exercise. Really got to play around and explore Docker and Ansible in a
  very practical situation.

  Some improvements that I can see being made is to make the docker containers persistent so the Ansible playbook will terminate
  and we can elminate the need to open another terminal and manually ssh into the vagrant box.
