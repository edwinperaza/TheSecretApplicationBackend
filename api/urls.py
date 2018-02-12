from django.conf.urls import url, include

from rest_framework.routers import DefaultRouter

from rest_framework_swagger.views import get_swagger_view

from users.viewsets import UserViewSet
from objectives.viewsets import ObjectiveViewSet
from countries.viewsets import CountryViewset
from languages.viewsets import LanguageViewset


schema_view = get_swagger_view(title='Objectives API')

router = DefaultRouter()
router.register(r'users', UserViewSet, 'user')
router.register(r'objectives', ObjectiveViewSet, 'objective')
router.register(r'objectives', ObjectiveViewSet, 'objective')
router.register(r'countries', CountryViewset, 'country')
router.register(r'languages', LanguageViewset, 'language')

urlpatterns = [
    url(r'^docs/?$', schema_view),
    url(r'^', include(router.urls)),
]
