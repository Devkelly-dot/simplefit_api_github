from .base import BaseModelSerializer
from dayPlan.models import Dayplan


class DayplanOutputSerializer(BaseModelSerializer):
    class Meta:
        model = Dayplan
        fields = [
            'id',
            'user',
            'day',
            'goal',
        ]
