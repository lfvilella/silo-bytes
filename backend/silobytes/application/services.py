import datetime

import pytz
from django.core import exceptions

from . import models


def set_storage_withdraw_to_now(storage_id):
    try:
        storage = models.Storage.objects.get(pk=storage_id)
    except models.Storage.DoesNotExist:
        raise None

    now = datetime.datetime.now(tz=pytz.utc)
    if storage.withdrawal_date <= now:
        return 'Withdrawal must be greater than now'

    try:
        storage.withdrawal_date = now
        storage.save()
    except exceptions.ValidationError as error:
        return error.message

    return storage
