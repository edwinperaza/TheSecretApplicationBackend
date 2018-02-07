from django.conf.urls import url, include

from rest_framework.routers import DefaultRouter

from rest_framework_jwt.views import obtain_jwt_token

from users.viewsets import UserViewSet
from objectives.viewsets import ObjectiveViewSet


router = DefaultRouter()
router.register(r'users', UserViewSet, 'user')
router.register(r'objectives', ObjectiveViewSet, 'objective')

urlpatterns = [
    url(r'^users/sign-in/', obtain_jwt_token),
    url(r'^', include(router.urls)),
]
