from rest_framework import serializers

from . import models


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Student
        fields = ['id', 'name', 'nickname', 'lastname', 'proflie_picture']