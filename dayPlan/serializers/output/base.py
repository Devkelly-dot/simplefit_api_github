from rest_framework import serializers

class NoSerializer:
    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return self.data

class BaseModelSerializer(serializers.ModelSerializer):
    pass