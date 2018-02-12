from rest_framework import viewsets

from countries_plus.models import Country

from .serializers import CountrySerializer


class CountryViewset(viewsets.ReadOnlyModelViewSet):
    model = Country
    serializer_class = CountrySerializer

    def get_queryset(self):
        return self.model.objects.all()
