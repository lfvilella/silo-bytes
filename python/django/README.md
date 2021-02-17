# Silo Bytes Django Project

[Django Docs](https://docs.djangopro


Needs docker installed.
# Guide to Run Locally


Build the project
```
$ make build

or

$ [ -f .env ] || cp template.env .env
$ docker-compose build
$ docker-compose up -d
$ docker-compose exec backend /bin/bash -c "./manage.py migrate"
```

Create a superuser
```
$ make createsuperuser

or

$ docker-compose exec backend /bin/bash -c "./manage.py createsuperuser"
```

Populate your database - Optional
```
$ make cmd
or
$ docker-compose exec backend /bin/bash
```
```
$ pip install -r requirements-dev.txt  # Optional...

$ python manage.py shell

>>> from core import populate
>>> populate.run()
```

*`Control + D` or `Control + C` to quit*
