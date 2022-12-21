# Skypro.Python

Бэкэнд для приложения для отслеживания задач

# Описание

### Stack

- django - backend
- postgresql - database
- Требования к разработке указаны в todolist/requirements.dev.txt

### Функции
1. Аутентификация и пользователь (основное приложение):
   - ВК Оаут `(в разработке)`
   - базовая аутентификация джанго
   - обновление профиля
   - изменение пароля
2.Основной интерфейс (приложение целей):
   - базовый CRUD с фильтрами и сортировкой: доски, цели, категории, комментарии
   - пользователь может просматривать элементы, связанные с досками, членом которых он является (владелец, писатель или читатель)
   - пользователь может создавать категории, цели, комментарии, только если он является владельцем/автором соответствующей доски
   - пользователь может обновлять, удалять, только если он является владельцем/писателем соответствующей доски
   - пользователь может обновлять, удалять только свои комментарии
   - когда доска, категория отмечена как is_deleted, все дочерние категории, цели также отмечены как is_deleted
3. Бот Telegram (бот-приложение):
   - пользователю необходимо подтвердить личность с помощью кода подтверждения
   - пользователь мог просматривать и создавать цели
   - имя пользователя в телеграмме бота: `(в разработке)`

## Как запустить проект в среде разработки

1. Создать виртуальную среду
2. Установить зависимости от requirements.dev.txt
   - `pip install -r todolist/requirements.dev.txt`
3. Установите переменные среды в .env file
   - Создайте .env файл в папке todolist
   - Вы можете скопировать переменные по умолчанию из todolist/.env.example
4. Запустить базу данных из папки развертывания
   - `cd deploy`
   - `docker compose --env-file ../todolist/.env -f docker-compose.db.yaml up -d`
5. Сделайте миграцию из папки todolist
   - `cd todolist`
   - `./manage.py makemigrations`
   - `./manage.py migrate`
6. Запустить проект
   - `./manage.py runserver`

#### Доступ к сайту администратора

1. Создать пользователя-администратора
   - `./manage.py createsuperuser`
   - установить значения и обязательные поля
2. Доступ к сайту администратора по адресу http://127.0.0.1:8000/admin/

## Как запустить проект в разработку с помощью Docker-compose

1. Создайте файл .docker_env в папке развертывания:
   - вы можете скопировать переменные по умолчанию из todolist/.env.example
   - обязательно установите для DB_HOST значение `db`, которое является именем контейнера.
2. Используйте docker-compose.dev.yaml из папки развертывания.
   - `cd deploy`
   - `docker compose --env-file .docker_env -f docker-compose.dev.yaml up -d`
3. Будет сделано следующее:
   - запустится контейнер postgresql
   - будут п**рименяться миграции
   - запустится API-контейнер
   - передний контейнер запустится

## Deploy

1. Deploy автоматизирован с github actions. 
2. Используемые файлы проекта:
   - actions**: .github/workflows/actions.yaml
   - compose file: deploy/docker-compose.ci.yaml
   - env variables: deploy/.ci_env
   - Переменные в файлах compose и env заменены секретами github
3. Docker hub images:
   - front: sermalenk/skypro-front:lesson-38
   - back: canbi4/todolists:<tag>
4. Добавить администратора при первом запуске:
   - подключиться к серверу и получить доступ к папке проекта
   - `docker exec -it <api container_id> /bin/bash`
   - `./manage.py createsuperuser`
5. Адреса:
   - front: http://todoi.ga
   - admin: http://todoi.ga/admin/
   - swagger: http://todoi.ga/api/schema/swagger-ui/

