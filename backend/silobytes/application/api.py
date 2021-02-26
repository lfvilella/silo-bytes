import knox.views
from django.contrib import auth
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import (
    decorators,
    filters,
    permissions,
    response,
    status,
    views,
    viewsets,
)
from rest_framework.authtoken.serializers import AuthTokenSerializer

from . import models, serializers, services


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
    http_method_names = ['get', 'patch']

    filterset_fields = ('quantity',)
    search_fields = ['^silo__name', '^client__name', '^product__name']

    @decorators.action(
        methods=['patch'],
        url_path='withdraw-now',
        url_name='withdraw-now',
        detail=True,
    )
    def set_withdraw_now(self, request, pk, format=None):
        storage = services.set_storage_withdraw_to_now(pk)
        if not storage:
            return response.Response(
                {'error': 'Storage Not Found.'},
                status=status.HTTP_404_NOT_FOUND,
            )

        if isinstance(storage, str):
            return response.Response(
                {'error': storage}, status=status.HTTP_400_BAD_REQUEST,
            )

        return response.Response(
            {'token': request.headers['Authorization'], 'pk': pk},
            status=status.HTTP_200_OK,
        )
