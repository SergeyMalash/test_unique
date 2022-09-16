from rest_framework import serializers

from app.models import TestIP


class TestIPSerializer(serializers.ModelSerializer):

    class Meta:
        model = TestIP
        fields = '__all__'
