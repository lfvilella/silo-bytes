import knox.views
from django.contrib import auth
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import (
    filters,
    permissions,
    viewsets,
    views,
    status,
    response,
)
from rest_framework.authtoken.serializers import AuthTokenSerializer

from . import models, serializers


class LoginAPI(knox.views.LoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        auth.login(request, user)
        return super(LoginAPI, self).post(request, format=None)


class VerifyAPI(views.APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        return response.Response(
            {'token': request.headers['Authorization']},
            status=status.HTTP_200_OK,
        )


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
