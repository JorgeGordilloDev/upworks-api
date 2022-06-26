from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static

from rest_framework_simplejwt.views import (
    TokenObtainPairView, TokenRefreshView, TokenVerifyView, TokenBlacklistView
)

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from apps.users.views import Login, Logout

schema_view = get_schema_view(
    openapi.Info(
        title="UpWorks API",
        default_version='v1',
        description="API Rest para UpWorks, la cual es una plataforma de bolsa de trabajo para la Universidad Politécnica de Tapachula",
        # terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="203102@uptapachulas.edu.mx"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/v1/logout/', Logout.as_view(), name = 'logout'),
    path('api/v1/login/',Login.as_view(), name = 'login'),

    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/v1/token/blacklist/', TokenBlacklistView.as_view(), name='token_blacklist'),

    path('api/v1/', include('apps.users.urls'), name='users'),

    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
