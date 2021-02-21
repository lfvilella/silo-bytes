from django.contrib import auth

from django_filters.rest_framework import DjangoFilterBackend
import knox.views
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework import permissions, viewsets, filters

from . import models, serializers


class LoginAPI(knox.views.LoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        auth.login(request, user)
        return super(LoginAPI, self).post(request, format=None)


class StorageViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = (
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    )
    queryset = models.Storage.objects.all().order_by('-created_at')
    serializer_class = serializers.StorageSerializer
    http_method_names = [
        'get',
    ]

    filterset_fields = ('quantity',)
    search_fields = ['^silo__name', '^client__name', '^product__name']
