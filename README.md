[![license](https://img.shields.io/github/license/lfvilella/silo-bytes.svg)](https://github.com/lfvilella/silo-bytes/blob/main/LICENSE)

# Silo Bytes

Prog2 project from UENP.
---

The object is to implement the silos control system.


### Simple Data Modeling

This project was thought to be easy for external comprehensions, that is it was not thought about scalability and future features.

![Screen Shot 2021-02-10 at 23 01 22](https://user-images.githubusercontent.com/45940140/107595602-ebaadb00-6bf3-11eb-9351-9e77bd002421.png)


### Simple Screens Design for App Mobile
[<img width="928" alt="Screen Shot 2021-02-24 at 12 06 09" src="https://user-images.githubusercontent.com/45940140/109020578-d5dbf200-7698-11eb-84fa-6acd20eb34f0.png">
](https://www.figma.com/file/C9ljnxN1BeChfeAzhyxb69/SiloBytes?node-id=0%3A1)


### Quick video about web system.
[<img width="1168" alt="Screen Shot 2021-02-19 at 11 12 07" src="https://user-images.githubusercontent.com/45940140/108514991-55d21880-72a3-11eb-8131-7c2c9722290f.png">](https://youtu.be/-iUIt0smZFA)


# Tech Stack
- [Pyhon](https://www.python.org/)
- [Django](https://docs.djangopro)
- [Django-Rest](https://www.django-rest-framework.org/)
- [React-Native](https://reactnative.dev/)
- [Docker](https://docs.docker.com/)
- [Docker-Compose](https://docs.docker.com/compose/install/)

# GIFs
![1](https://user-images.githubusercontent.com/45940140/109242808-9279a480-77ba-11eb-9cdb-d9dedf653ff7.gif)
![2](https://user-images.githubusercontent.com/45940140/109242818-96a5c200-77ba-11eb-89dc-d928f3e0e622.gif)
![3](https://user-images.githubusercontent.com/45940140/109242827-986f8580-77ba-11eb-9e39-dfd00ef135da.gif)
![4](https://user-images.githubusercontent.com/45940140/109242843-9c9ba300-77ba-11eb-8a9e-d935adfeb205.gif)
![5](https://user-images.githubusercontent.com/45940140/109242849-a02f2a00-77ba-11eb-9827-b0ffca4bfbf8.gif)

# Backend Guide to Run Locally

*Needs docker installed.*

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


Run tests
```
make test

or

$ docker-compose exec backend /bin/bash -c "./manage.py test"
```
