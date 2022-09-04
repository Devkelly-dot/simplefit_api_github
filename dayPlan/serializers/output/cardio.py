from .base import BaseModelSerializer
from dayPlan.models import Cardio


class CardioOutputSerializer(BaseModelSerializer):
    class Meta:
        model = Cardio
        fields = [
            'id',
            'name',
            'description',
            'complete',
            'goal',
            'measurement'
        ]
