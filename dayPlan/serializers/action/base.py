from rest_framework import serializers
from django.http import JsonResponse

class BaseActionSerializer(serializers.Serializer):
    action_serializer = None




