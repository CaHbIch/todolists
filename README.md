# Skypro.Python course
## Coursework 6 - Todolist

Backend for task-tracking application

# Description

### Stack

- django - backend
- postgresql - database
- development requirements are specified in todolist/requirements.dev.txt

### Features

1. Authentication and User (core app):
   - VK Oauth
   - basic django authentication
   - profile update
   - password change
2. Main interface (goals app):
   - basic CRUD with filters and sorting: boards, goals, categories, comments
   - user can view items related to the boards he's member of (owner, writer or reader)
   - user can create categories, goals, comments only if he's owner/writer of the related board
   - user can update, delete only if he's owner/writer of the related board
   - user can update, delete only his comments
   - when board, category is marked as is_deleted, all child categoris, goals are also marked as is_deleted
3. Telegram bot (bot app):
   - user need to verify identity using verification code
   - user could view and create goals
   - bot telegram username: @TodolistT1000Bot

## How to launch project in development environment

1. Create virtual environment
2. Install dependencies from requirements.dev.txt
   - `pip install -r todolist/requirements.dev.txt`
3. Set environment variables in .env file
   - create .env file in todolist folder
   - you can copy the default variables from todolist/.env.example
4. Launch database from deploy folder
   - `cd deploy`
   - `docker compose --env-file ../todolist/.env -f docker-compose.db.yaml up -d`
5. Make migrations from todolist folder
   - `cd todolist`
   - `./manage.py makemigraitons`
   - `./manage.py migrate`
6. Launch project
   - `./manage.py runserver`

#### Accessing admin site

1. Create admin-user
   - `./manage.py createsuperuser`
   - set values and required fields
2. Access admin site at http://127.0.0.1:8000/admin/

## How to launch project in development with Docker-compose

1. Создайте файл .docker_env в папке развертывания:
   - вы можете скопировать переменные по умолчанию из todolist/.env.example
   - обязательно установите для DB_HOST значение `db`, которое является именем контейнера.
2. Используйте docker-compose.dev.yaml из папки развертывания.
   - `cd deploy`
   - `docker compose --env-file .docker_env -f docker-compose.dev.yaml up -d`
3. Будет сделано следующее:
   - запустится контейнер postgresql
   - будут применяться миграции
   - запустится API-контейнер
   - передний контейнер запустится

## Deploy

1. Deploy is automated with github actions. 
2. Project files used:
   - actions: .github/workflows/actions.yaml
   - compose file: deploy/docker-compose.ci.yaml
   - env variables: deploy/.ci_env
   - variables in compose and env files are replaced with github secrets
3. Docker hub images:
   - front: sermalenk/skypro-front:lesson-38
   - back: kpaveliev/skypro-c06-cw06-todolist:<tag>
4. To add admin during first launch:
   - connect to server and access project folder
   - `docker exec -it <api container_id> /bin/bash`
   - `./manage.py createsuperuser`
5. Addresses:
   - front: http://todoi.ga
   - admin: http://todoi.ga/admin/
   - swagger: http://todoi.ga/api/schema/swagger-ui/
   

