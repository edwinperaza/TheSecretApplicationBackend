from django.conf.urls import url, include

from rest_framework.routers import DefaultRouter

from rest_framework_swagger.views import get_swagger_view

from rest_framework_jwt.views import obtain_jwt_token

from users.viewsets import UserViewSet
from objectives.viewsets import ObjectiveViewSet


schema_view = get_swagger_view(title='Objectives API')

router = DefaultRouter()
router.register(r'users', UserViewSet, 'user')
router.register(r'objectives', ObjectiveViewSet, 'objective')

urlpatterns = [
    url(r'^docs/?$', schema_view),
    url(r'^', include(router.urls)),
]
