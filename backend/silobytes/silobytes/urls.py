import knox.views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.shortcuts import redirect
from django.urls import include, path

from application import api, routes


def go_to_admin(request):
    return redirect('admin/')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', go_to_admin),
    path('api/', include(routes.router.urls)),
    path('api/auth/login/', api.LoginAPI.as_view(), name='login'),
    path('api/auth/logout/', knox.views.LogoutView.as_view(), name='logout'),
    path(
        'api/auth/logoutall/',
        knox.views.LogoutAllView.as_view(),
        name='logoutall',
    ),
]


admin.site.site_header = 'Silo Bytes'
admin.site.index_title = 'Administration'
admin.site.site_title = 'Silo Bytes'

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
