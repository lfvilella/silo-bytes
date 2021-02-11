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
        return self.name


class Silo(core.models.BaseModel):
    name = models.CharField(max_length=255, null=False, blank=False)
    description = models.CharField(max_length=255, null=True, blank=True)
    size = models.FloatField(null=False, blank=False)

    def __str__(self):
        return f'{self.name} - {self.size}'


class Storage(core.models.BaseModel):
    client = models.ForeignKey('Client', on_delete=models.CASCADE)
    silo = models.ForeignKey('Silo', on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    quantity = models.FloatField(null=False, blank=False)
    entry_date = models.DateTimeField(auto_now_add=True)
    withdrawal_date = models.DateTimeField()
    payment_method = models.CharField(
        max_length=20,
        choices=choices.PAYMENT_METHOD_CHOICES,
        null=True,
        blank=True,
        default=choices.MONEY,
    )
    status = models.CharField(
        max_length=20,
        choices=choices.STATUS_CHOICES,
        default=choices.STATUS_OPEN,
    )

    def __str__(self):
        return f'{self.client.name} - {self.silo.name}'
