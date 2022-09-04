from dayPlan.serializers.output import LiftOutputSerializer
from dayPlan.serializers.action import LiftUpdateSerializer, LiftDeleteSerializer

from dayPlan.models import Lift
from .base import PostView

class LiftUpdate(PostView):
    model = Lift
    login_required = True
    optional_fields = ["name","description","goal","weight","reps","complete","measurement"]
    output_serializer = LiftOutputSerializer
    action_serializer = LiftUpdateSerializer

class LiftDelete(PostView):
    model = Lift
    login_required = True
    output_serializer = LiftOutputSerializer
    action_serializer = LiftDeleteSerializer
