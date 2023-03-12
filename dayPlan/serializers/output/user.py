from .base import BaseModelSerializer
from dayPlan.models import User
from rest_framework.authtoken.models import Token
from rest_framework import serializers

class UserOutputSerializer(BaseModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email'
        ]

class TokenOutputSerializer(BaseModelSerializer):
    token = serializers.CharField(source = 'key')
    
    class Meta:
        model = Token
        fields = [
            'token'
        ]
    
    def to_representation(self, instance):
        data = super().to_representation(instance)
        return {'token': data['token']}