# Welcome to Docker Workshop!
A brief introduction to Docker in collaboration with AAII.

<img src="https://raw.githubusercontent.com/roniepaolo/aaii-docker-workshop/master/images/docker_workshop.png" alt="drawing" width="1000"/>

## Docker Commands
These are some useful commands that we constantly use when working with docker.

### 1. Basic Commands
* List active docker processes: ``` docker ps ```
* List all docker processes: ``` docker ps -a```
* List images: ``` docker images ```
* Pull images: ``` docker pull <image>:<tag> ```
* Run a cotainer: ``` docker run -it <image>:<tag> <command> ```
* Execute a command in a container (It can be used for entering to a container in a new session PID X): ``` docker exec -it <container> <command>```
* Enter to a running container (PID 1): ``` docker attach <containerid>```
* Stop a running container: ``` docker stop <container>```
* Start a stopped container: ``` docker start <container>```
* Remove image: ``` docker rmi <image_id>```
* Remove container: ``` docker rm <container_id>```

### 2. Dockerfiles
* Docker build: ``` docker build -f docker/Dockerfile -t <image>:<version> <context> ```
* Docker run with autoremove: ``` docker run --rm -it --volume $(pwd)/<file_or_directory>:/<file_or_directory> <image>:<version> <command> ```

### 3. Docker Compose
* Docker compose up with deamon: ``` docker-compose up -d ```
* Docker compose down: ``` docker-compose down ```
* Execute a command in a container (It can be used for entering to a container in a new session PID X): ``` docker-compose exec <service> <command> ```
* Check the log: ``` docker-compose logs --tail <number_of_lines_to_show> ```
