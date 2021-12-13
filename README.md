# News Post API

## Steps to run a project:
## 1. Install all packages from requirements.txt file.

```
$ pip install -r requirements.txt
```

## 2. Apply all migrations and create superuser.

```
$ python3 manage.py makemigrations
$ python3 manage.py migrate
$ python3 manage.py migrate django_celery_beat
$ python3 manage.py createsuperuser
```

## 3. Run Celery worker in background.

```
$ celery -A news worker --beat --scheduler django --loglevel=info
```

## 4. Run Django project.

```
$ python3 manage.py runserver
```

## Change Periodic task time interval from Admin panel functionality.
### You can easily change time interval of Periodic task that resets upvotes from admin panel.

## Heroku Link
 [https://news-api-test.herokuapp.com](https://news-api-test.herokuapp.com)

## Postman Collection Link
[https://www.getpostman.com/collections/08a40ac6394427b330f9](https://www.getpostman.com/collections/08a40ac6394427b330f9)