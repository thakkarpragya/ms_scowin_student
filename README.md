## Run in local system

#### Pre-requisites

> `Rabbitmq` service should be up and running.

#### Steps to run:

Clone the repository and install the required packages using below commands
```sh
git clone git@github.com:thakkarpragya/ms_scowin_student.git
cd ms_scowin_student
```

Check if pip is installed

```sh
pip --version
```

Install all the required packages

```sh
pip install -r requirements.txt
```

Start the server

```sh
python manage.py runserver <port>
```

Verify the deployment by navigating to your server address in your preferred browser

```sh
127.0.0.1:<port>
```

## Run as docker container

#### Steps to run:

Build the Dockerfile

```
DOCKER_BUILDKIT=0 docker build . -t <image-name> --no-cache
```

Run rabbitmq and image (in the same order)
```
docker run -d --hostname rabbit_mq --name rabbit_mq -p 15672:15672 -p  5672:5672 rabbitmq:3.8-rc-management
docker run -d -p 8084:8084 <image-name>
```

Verify the deployment by navigating to your server address in your preferred browser.

```sh
127.0.0.1:8084
```

## Run application E2E using Docker

#### Pre-requisites:
> - Verify that no container named `rabbit_mq` is running in your system.
> - If producer and consumer microservices are cloned to local, make sure all the repositories are in same location for volume mount.
> - Else, comment out volume mount configuration in docker-compose.yml.
> - Please note that if volume mount configuration(s) is/are commented out, data that are published in queue and consumed from the queue will be lost once the `docker-compose` is stopped.

#### Steps to run:

Start docker compose
```
docker-compose up --remove-orphans
```

Verify that the containers are running in your system.
<!-- Below command should show rabbitmq, publisher and consumer containers in running state -->
```
docker ps 
```

Navigate to the below links in your preferred browser
```
RabbitMQ - http://127.0.0.1:15672
Publisher (Student Microservice) - http://127.0.0.1:8084
Consumer (Vaccination Microservice)- http://127.0.0.1:8085
```

Verify that the communication between rabbitmq, publisher and consumer(s) happen by triggering a POST API call to /students (with id \<id\>) in publisher and a GET API call to /students/\<id\> in consumer.


## Run application E2E using Kubernetes

#### Pre-requisites:
> minikube is installed and started in system using `minikube start` command.
> kompose is installed in the system.

#### Steps to run:

Convert config from docker compose to kubernetes.
```sh
kompose convert
Note: If you have the list of config files to be deployed in kubernetes, this step can be skipped.
```

A list of files containing service and pod configurations will be generated. Deploy in kubernetes using `kubectl` command.
```sh
kubectl apply -f file1,file2,...,fileN
Note: file1,fil2,...,fileN should not contain spaces in-between.
```

View the status of pods and services in minikube dashboard.
```sh
minikube dashboard
```
