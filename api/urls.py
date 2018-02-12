from django.conf.urls import url, include

from rest_framework.routers import DefaultRouter

from rest_framework_swagger.views import get_swagger_view

from users.viewsets import UserViewSet
from objectives.viewsets import ObjectiveViewSet
from countries.viewsets import CountryViewset


schema_view = get_swagger_view(title='Objectives API')

router = DefaultRouter()
router.register(r'users', UserViewSet, 'user')
router.register(r'objectives', ObjectiveViewSet, 'objective')
router.register(r'objectives', ObjectiveViewSet, 'objective')
router.register(r'countries', CountryViewset, 'country')

urlpatterns = [
    url(r'^docs/?$', schema_view),
    url(r'^', include(router.urls)),
]
