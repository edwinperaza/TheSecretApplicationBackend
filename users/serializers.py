from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('email', 'password')

    def create(self, validated_data):
        user = User.objects.create(
            email=validated_data.get('email')
        )

        user.set_password(validated_data.get('password'))
        user.save()

        return user
