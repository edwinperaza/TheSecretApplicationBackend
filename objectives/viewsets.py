from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

from .models import Objective
from .serializers import ObjectiveSerializer


class ObjectiveViewSet(viewsets.ModelViewSet):
    model = Objective
    serializer_class = ObjectiveSerializer

    def get_queryset(self):
        return self.model.objects.select_related(
            'user',
        ).all()

    def create(self, request, *args, **kwargs):
        data = request.data.copy()
        data['user_id'] = request.user.pk
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
