from .base import BaseModelSerializer
from dayPlan.models import Food


class FoodOutputSerializer(BaseModelSerializer):
    class Meta:
        model = Food
        fields = [
            'id',
            'name',
            'description',
            'complete'
        ]
