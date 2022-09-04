from .base import BaseModelSerializer
from dayPlan.models import Lift


class LiftOutputSerializer(BaseModelSerializer):
    class Meta:
        model = Lift
        fields = [
            'id',
            'name',
            'description',
            'complete',
            'goal',
            'weight',
            'reps',
            'measurement'
        ]
