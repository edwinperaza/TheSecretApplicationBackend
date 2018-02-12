from django.utils.translation import ugettext_lazy as _

from rest_framework import serializers

from .models import User


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name',
            'password',
            'birthday',
            'language',
            'country',
        )

    def create(self, validated_data):
        first_name = validated_data.get(
            'first_name') or validated_data.get('firstName')
        last_name = validated_data.get(
            'last_name') or validated_data.get('lastName')

        user = User.objects.create(
            email=validated_data.get('email'),
            first_name=first_name or '',
            last_name=last_name or '',
        )

        user.set_password(validated_data.get('password'))
        user.save()

        return user


class UserValidatePasswordSerializer(UserCreateSerializer):
    validate_password = serializers.CharField(write_only=True)

    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = UserCreateSerializer.Meta.fields + (
            'validate_password',
        )

    def validate(self, data):
        password = data.get('password')
        validate_password = data.get('validate_password')
        if (password and validate_password and
                not password == validate_password):
            raise serializers.ValidationError(
                _("The two password fields didn't match.")
            )
        return data
