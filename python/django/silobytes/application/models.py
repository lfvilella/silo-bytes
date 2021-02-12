import datetime

from django.core import exceptions
from django.db import models

import core.models

from . import choices


class Client(core.models.BaseModel):
    name = models.CharField(max_length=255, null=False, blank=False)
    email = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return f'{self.name} - {self.phone}'


class Product(core.models.BaseModel):
    name = models.CharField(max_length=255, null=False, blank=False)
    description = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f'{self.pk} - {self.name}'


class Silo(core.models.BaseModel):
    name = models.CharField(max_length=255, null=False, blank=False)
    description = models.CharField(max_length=255, null=True, blank=True)
    size = models.FloatField(null=False, blank=False)

    def __str__(self):
        return f'{self.name} - {self.size}t'


class Storage(core.models.BaseModel):
    client = models.ForeignKey('Client', on_delete=models.CASCADE)
    silo = models.ForeignKey('Silo', on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    annotations = models.TextField(null=True, blank=True)
    quantity = models.FloatField(null=False, blank=False)
    entry_date = models.DateTimeField(auto_now_add=True)
    withdrawal_date = models.DateTimeField()
    payment_method = models.CharField(
        max_length=20,
        choices=choices.PAYMENT_METHOD_CHOICES,
        null=True,
        blank=True,
    )
    status = models.CharField(
        max_length=20,
        choices=choices.STATUS_CHOICES,
        default=choices.STATUS_OPEN,
    )

    def __str__(self):
        return f'{self.client.name} - {self.silo.name}'

    def clean_entry_date(self):
        if self.withdrawal_date and self.entry_date >= self.withdrawal_date:
            raise exceptions.ValidationError(
                'Entry date can not be greater or equal than withdrawal date.'
            )

    def clean_withdrawal_date(self):
        if self.withdrawal_date and self.withdrawal_date <= self.entry_date:
            raise exceptions.ValidationError(
                'Withdrawal date can not be less or equal than entry date.'
            )

    def clean_quantity(self):
        if self.quantity > self.silo.size:
            raise exceptions.ValidationError(
                'This quantity does not fit in the silo.'
            )

    def clean_silo(self):
        _storages = Storage.objects.filter(
            silo=self.silo, status=choices.STATUS_OPEN,
        )

        now = datetime.datetime.now()
        exist_storage = _storages.filter(withdrawal_date__gte=now).last()
        if exist_storage and exist_storage.pk != self.pk:
            raise exceptions.ValidationError(
                'Can not create a new storage, because this Silo '
                f'already being used on "{exist_storage.silo.name}".'
            )

        forgot_storage = _storages.last()
        if forgot_storage and forgot_storage.pk != self.pk:
            # when expire the withdrawal_date but status is open.
            raise exceptions.ValidationError(
                'Can not create a new storage, because this Silo '
                f'already being used on "{forgot_storage.silo.name}". '
                'Please update the withdrawal date or mark status open '
                f'on Storage "{self.pk}".'
            )

    def clean(self):
        self.clean_entry_date()
        self.clean_withdrawal_date()
        self.clean_silo()
        self.clean_quantity()

    def save(self, *args, **kwargs):
        self.clean()
        return super(Storage, self).save(*args, **kwargs)
