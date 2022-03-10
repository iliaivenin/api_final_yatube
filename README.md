# REST API Yatube
API включает в себя посты, комментарии, подписчиков и группы. Авторизация реализованна через JWT-токен.

## Стек технологий
Python, Django, Django REST Framework, SQLite3, Simple JWT, Django Filter.

## Установка
Создайте виртуальное окружение:
```bash
python -m venv venv
```
Активируйте его:
```bash
source venv/Scripts/activate
```
Используйте [pip](https://pip.pypa.io/en/stable/), чтобы установить зависимости:
```bash
pip install -r requirements.txt
```
Примените миграции:
```bash
python manage.py migrate
```
И запускайте сервер:
```bash
python manage.py runserver
```

## Вход
Создайте супер пользователя, обязательно укажите имя пользователя и пароль:
```bash
python manage.py createsuperuser
```

Отправьте POST-запрос, с именем пользователя и паролем на ```http://127.0.0.1:8000/api/v1/token/```, чтобы получить токен. Пример:
```bash
curl -X POST -F "username=ваше_имя_пользователя" -F "password=ваш_пароль" http://127.0.0.1:8000/api/v1/token/
```

## Документация
Чтобы открыть документацию, запустите сервер и перейдите по ссылке:
```http://127.0.0.1:8000/redoc/```
