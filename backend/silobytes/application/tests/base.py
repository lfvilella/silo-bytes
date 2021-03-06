import datetime
import random
import uuid

import pytz
import rest_framework.test
from django.contrib.auth.models import User

from application import models


class BaseTest(rest_framework.test.APITestCase):
    def setUp(self):
        self.user = self.create_fake_user(
            'Luffy', 'monkeydluffy@mail.com', 'OnePiece'
        )
        self.internal_client = self.create_fake_client()
        self.silo = self.create_fake_silo()
        self.product = self.create_fake_product()

    def authenticate(self, user_data=None):
        if not user_data:
            user_data = {'username': 'Luffy', 'password': 'OnePiece'}

        token = self.client.post('/api/auth/login/', data=user_data).json()
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {token["token"]}')

    def create_fake_user(self, username, email, password):
        user = User.objects.create_user(username, email, password)
        return user

    def create_fake_client(self, name=None, email=None, phone=None):
        if not name:
            name = f'name - {uuid.uuid4()}'
        if not email:
            email = f'email - {uuid.uuid4()}'
        if not phone:
            phone = f'phone - {uuid.uuid4()}'

        return models.Client.objects.create(
            name=name, email=email, phone=phone,
        )

    def create_fake_product(self, name=None, description=None):
        if not name:
            name = f'name - {uuid.uuid4()}'
        if not description:
            description = f'description - {uuid.uuid4()}'

        return models.Product.objects.create(
            name=name, description=description,
        )

    def create_fake_silo(self, name=None, description=None, size=None):
        if not name:
            name = f'name - {uuid.uuid4()}'
        if not description:
            description = f'description - {uuid.uuid4()}'
        if not size:
            size = random.randint(500, 900)

        return models.Silo.objects.create(
            name=name, description=description, size=size,
        )

    def create_fake_storage(
        self,
        client=None,
        silo=None,
        product=None,
        quantity=None,
        price_per_day=None,
        entry_date=None,
        withdrawal_date=None,
    ):
        now = datetime.datetime.now(tz=pytz.utc)

        if not client:
            client = self.internal_client
        if not silo:
            silo = self.silo
        if not product:
            product = self.product
        if not quantity:
            quantity = random.randint(100, 450)
        if not price_per_day:
            price_per_day = round(random.uniform(100, 200), 2)
        if not entry_date:
            entry_date = now
        if not withdrawal_date:
            withdrawal_date = now.replace(month=now.month + 1)

        return models.Storage.objects.create(
            client=client,
            silo=silo,
            product=product,
            quantity=quantity,
            price_per_day=price_per_day,
            entry_date=entry_date,
            withdrawal_date=withdrawal_date,
        )
