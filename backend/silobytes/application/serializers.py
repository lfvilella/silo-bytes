from django.contrib.auth.models import User
from rest_framework import serializers

from . import models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')


class SiloSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Silo
        fields = ('id', 'name', 'description', 'size')


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = ('id', 'name', 'description')


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Client
        fields = ('id', 'name', 'email', 'phone')


class StorageSerializer(serializers.ModelSerializer):
    silo = serializers.PrimaryKeyRelatedField(
        queryset=models.Silo.objects.all()
    )

    class Meta:
        model = models.Storage
        fields = (
            'id',
            'client',
            'silo',
            'product',
            'annotations',
            'quantity',
            'price_per_day',
            'entry_date',
            'withdrawal_date',
            'payment_method',
            'status',
            'current_cost',
            'total_cost',
        )

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['client'] = ClientSerializer(
            instance=instance.client
        ).data
        representation['silo'] = SiloSerializer(instance=instance.silo).data
        representation['product'] = ProductSerializer(
            instance=instance.product
        ).data
        return representation
