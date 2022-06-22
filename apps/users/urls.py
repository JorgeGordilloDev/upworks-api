from rest_framework.routers import DefaultRouter
from apps.users.views import *

router = DefaultRouter()

router.register(r'users', UserViewSet, basename='users')

urlpatterns = router.urls