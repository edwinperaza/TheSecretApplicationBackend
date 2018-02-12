from rest_framework import viewsets

from .models import Language

from .serializers import LanguageSerializer


class LanguageViewset(viewsets.ReadOnlyModelViewSet):
    model = Language
    serializer_class = LanguageSerializer

    def get_queryset(self):
        return self.model.objects.all()
