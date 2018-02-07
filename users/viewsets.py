from django.contrib.auth.forms import PasswordResetForm

from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework.decorators import list_route
from rest_framework import status

from .serializers import UserSerializer

from .models import User


class UserViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin):
    model = User
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny,)

    @list_route(methods=['post'])
    def password(self, request):
        form = PasswordResetForm(request.data)
        if form.is_valid():
            form.save(email_template_name=template_name, request=request)
        return Response({}, status.HTTP_200_OK)
