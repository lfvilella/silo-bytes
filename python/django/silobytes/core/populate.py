import datetime

import pytz

from application import models


def create_clients():
    clients = {
        'William': '551199695949392',
        'James': '551199695949392',
        'Harper': '551199695949392',
        'Mason': '551199695949392',
        'Evelyn': '551199695949392',
        'Ella': '551199695949392',
        'Jackson': '551199695949392',
        'Avery': '551199695949392',
    }
    for name, phone in clients.items():
        models.Client.objects.create(name=name, phone=phone)


def create_products():
    products = [
        'soy',
        'wheat',
        'barley',
    ]
    for product in products:
        models.Product.objects.create(name=product)


def create_silos():
    silos = {
        'Silo 1': 500,
        'Silo 2': 400,
        'Silo 3': 300,
        'Silo 4': 900,
    }
    for name, size in silos.items():
        models.Silo.objects.create(name=name, size=size)


def create_storage(
    client=None, silo=None, product=None, entry_date=None, withdrawal_date=None
):
    if not client:
        client = models.Client.objects.last()
    if not silo:
        silo = models.Silo.objects.last()
    if not product:
        product = models.Product.objects.last()

    now = datetime.datetime.now(tz=pytz.utc)
    if not withdrawal_date:
        withdrawal_date = now.replace(month=now.month + 1)
    if not entry_date:
        entry_date = now

    try:
        models.Storage.objects.create(
            client=client,
            silo=silo,
            product=product,
            quantity=200,
            price_per_day=4,
            entry_date=entry_date,
            withdrawal_date=withdrawal_date,
        )
    except Exception as error:  # models validation...
        print('Failed on Storage creation...')
        print(error)


def run():
    create_clients()
    create_products()
    create_silos()
    create_storage()
