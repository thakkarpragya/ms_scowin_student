## Run in local system

#### Pre-requisites

> `Rabbitmq` service should be up and running.

#### Steps to reproduce:

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

#### Pre-requisites:
> Verify that no container named `rabbit_mq` is running in your system.

Start docker compose
```
docker-compose up --remove-orphans
```

Verify that the containers are running in your system.
<!-- Below command should run rabbitmq and publisher containers -->
```
docker ps 
```

Navigate to the below links in your preferred browser
```
RabbitMQ - http://127.0.0.1:15672
Publisher - http://127.0.0.1:8084
```

Verify that the communication between publisher and rabbitmq happens by triggering a POST API call to /students.
