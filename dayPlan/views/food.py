from dayPlan.serializers.output import FoodOutputSerializer
from dayPlan.serializers.action import FoodUpdateSerializer, FoodDeleteSerializer

from dayPlan.models import Food
from .base import PostView

class FoodUpdate(PostView):
    model = Food
    login_required = True
    optional_fields = ["name","description","complete"]
    output_serializer = FoodOutputSerializer
    action_serializer = FoodUpdateSerializer

class FoodDelete(PostView):
    model = Food
    login_required = True
    output_serializer = FoodOutputSerializer
    action_serializer = FoodDeleteSerializer