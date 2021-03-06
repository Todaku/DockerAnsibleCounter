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
      Flask -> Framework for python webapps; provides simple, flexible way to set up a web app.
      redis -> A datastore that is persistent across different docker containers (useful for maintaining counter)
      docker-compose -> Automate running the Docker containers

- Running everything

    Items within the current directory

      main/sub --> two different containers
        main - one container which increments the hit counter on the webapps
        sub  - the other container with resets the same counter
      docker-compose.yml --> the config file for docker-compose; builds both the main/sub docker containers
      ansible/ --> directory not used in this segment. See Task2

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

    Ansible setup:

      sudo apt-get update
      sudo apt-get install software-properties-common
      sudo apt-add-repository ppa:ansible/ansible
      sudo apt-get update
      sudo apt-get install ansible

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

  One of the points of issue I encountered was an issue with my playbook that handled running the docker-compose task.
  The issue was when the playbook gets to that specific task, the playbook would not finish its run without a user termination
  (ctrl+c). This issue was quickly patched up by including the "-d" flag within the command call; this runs docker in the background (the daemon) and allows Ansible to finish the playbook. Without this, I had to use another terminal window and ssh into the vagrant box to manually verify the correctness.
  
  In addition to reflecting on the issues I faced, some potential issues I see would be scalability/configuration drift. I mention these two because they correlate with an issue of moving forward in the lifeline of this implementation. I am a novice with these technologies, so I did not make scalability a priority in my implementation. Additional as the project scales, configuration drift may happen through small updates that result in broken functionality. 

  Additionally, I think it would be valuable to consider alternative solutions to implementation. Possible alternatives would be without the usage of Flash/redis to bring up the python app. I happened to read on those and believed that they would be appropriate for the task, but there is more room to explore.

  Thanks for following along!
