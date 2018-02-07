from rest_framework import viewsets

from .models import Objective
from .serializers import ObjectiveSerializer


class ObjectiveViewSet(viewsets.ModelViewSet):
    model = Objective
    serializer_class = ObjectiveSerializer

    def get_queryset(self):
        return self.model.objects.select_related(
            'user',
        ).all()
