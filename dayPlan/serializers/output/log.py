from .base import BaseModelSerializer
from dayPlan.models import Log


class LogOutputSerializer(BaseModelSerializer):
    class Meta:
        model = Log
        fields = [
            'id',
            'date',
            'calories',
            'lift',
            'cardio',
        ]
