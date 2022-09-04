from .base import BaseModelSerializer
from dayPlan.models import User


class UserOutputSerializer(BaseModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email'
        ]
