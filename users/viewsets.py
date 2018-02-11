from django.contrib.auth.forms import PasswordResetForm

from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework.decorators import list_route
from rest_framework import status

from rest_framework_jwt.serializers import JSONWebTokenSerializer

from .serializers import UserCreateSerializer

from .models import User


class UserViewSet(
        viewsets.GenericViewSet,
        mixins.CreateModelMixin,
        mixins.DestroyModelMixin):
    model = User
    serializer_class = UserCreateSerializer

    def create(self, request, *args, **kwargs):
        user_serializer = self.get_serializer(data=request.data)
        user_serializer.is_valid(raise_exception=True)
        self.perform_create(user_serializer)
        headers = self.get_success_headers(user_serializer.data)
        serializer = JSONWebTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.object['user'] = user_serializer.data
        return Response(
            serializer.object,
            status=status.HTTP_201_CREATED,
            headers=headers,
        )

    @list_route(methods=['post'], url_path='sign-in')
    def sign_in(self, request):
        serializer = JSONWebTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user_serializer = self.get_serializer(serializer.object['user'])
        serializer.object['user'] = user_serializer.data
        return Response(
            serializer.object,
            content_type='application/json',
            status=status.HTTP_200_OK,
        )

    @list_route(methods=['post'], url_path='sign-out')
    def sign_out(self, request):
        return Response({}, status=status.HTTP_200_OK)

    @list_route(methods=['get'], permission_classes=(IsAuthenticated,))
    def current(self, request):
        serializer = self.get_serializer(self.request.user)
        return Response(serializer.data)

    @list_route(methods=['post'])
    def password(self, request):
        form = PasswordResetForm(request.data)
        if form.is_valid():
            template_name = 'registration/password_reset_done.pug'
            form.save(email_template_name=template_name, request=request)
        return Response({}, status.HTTP_200_OK)
