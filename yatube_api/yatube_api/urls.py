from django.contrib import admin
from django.urls import include, path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from django.conf.urls import url
from django.views.generic import TemplateView

schema_view = get_schema_view(
    openapi.Info(
        title="Yatube API",
        default_version='v1',
        description="Документация для приложения API проекта Yatube",
        contact=openapi.Contact(email="kirsan94@yandex.ru"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path(
        'redoc/',
        TemplateView.as_view(template_name='redoc.html'),
        name='redoc'
    ),
]


urlpatterns += [
    url(r'^api/v1/swagger(?P<format>\.json|\.yaml)$',
        schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^api/v1/swagger/$', schema_view.with_ui('swagger', cache_timeout=0),
        name='schema-swagger-ui'),
    url(r'^api/v1/redoc/$', schema_view.with_ui('redoc', cache_timeout=0),
        name='schema-redoc'),
]
