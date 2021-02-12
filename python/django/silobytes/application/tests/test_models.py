import datetime

import pytz
from django.core import exceptions

from application import models

from . import base


class TestStorage(base.BaseTest):
    def test_create_with_quantity_greater_than_silo_size_raises(self):
        silo = self.create_fake_silo(size=200)
        with self.assertRaises(exceptions.ValidationError):
            models.Storage.objects.create(silo=silo, quantity=300)

    def test_create_with_entry_date_greater_than_withdrawal_date_raises(self):
        now = datetime.datetime.now(tz=pytz.utc)
        entry_date = now + datetime.timedelta(hours=10)
        withdrawal_date = now

        with self.assertRaises(exceptions.ValidationError):
            self.create_fake_storage(
                entry_date=entry_date, withdrawal_date=withdrawal_date,
            )

    def test_update_with_withdrawal_date_less_than_entry_date_raises(self):
        now = datetime.datetime.now(tz=pytz.utc)
        entry_date = now - datetime.timedelta(hours=10)
        storage = self.create_fake_storage(entry_date=entry_date)

        withdrawal_date = now - datetime.timedelta(hours=5)
        storage.withdrawal_date = withdrawal_date
        with self.assertRaises(exceptions.ValidationError):
            storage.save()

    def test_create_with_silo_used_raises(self):
        storage = self.create_fake_storage()

        with self.assertRaises(exceptions.ValidationError):
            models.Storage.objects.create(silo=storage.silo)

    def test_create_with_silo_used_and_withdrawal_date_expired_raises(self):
        now = datetime.datetime.now(tz=pytz.utc)
        storage = self.create_fake_storage(
            entry_date=now - datetime.timedelta(hours=10),
            withdrawal_date=now - datetime.timedelta(hours=5),
        )

        with self.assertRaises(exceptions.ValidationError):
            models.Storage.objects.create(silo=storage.silo)

    def test_update_dont_raises(self):
        storage = self.create_fake_storage()

        product = self.create_fake_product()
        client = self.create_fake_client()

        storage.product = product
        storage.client = client
        storage.save()
        storage.refresh_from_db()

        self.assertEquals(storage.product, product)
        self.assertEquals(storage.client, client)

    def test_update_withdrawal_date_dont_raises(self):
        now = datetime.datetime.now(tz=pytz.utc)
        storage = self.create_fake_storage(
            entry_date=now - datetime.timedelta(hours=10),
            withdrawal_date=now - datetime.timedelta(hours=5),
        )

        date = storage.withdrawal_date.replace(
            month=storage.withdrawal_date.month + 1
        )
        storage.withdrawal_date = date
        storage.save()
        storage.refresh_from_db()
        self.assertEquals(
            date.isoformat(), storage.withdrawal_date.isoformat()
        )
