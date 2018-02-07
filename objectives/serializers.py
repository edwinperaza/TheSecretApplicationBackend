from rest_framework import serializers

from .models import Objective


class ObjectiveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Objective
        fields = (
            'id',
            'user_id',
            'title',
            'description',
            'until_date',
            'created_at',
        )
