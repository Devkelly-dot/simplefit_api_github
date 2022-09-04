from dayPlan.serializers.output import CardioOutputSerializer
from dayPlan.serializers.action import CardioUpdateSerializer, CardioDeleteSerializer

from dayPlan.models import Cardio
from .base import BaseViewSet, PostView

class CardioViewSet(BaseViewSet):
    model = Cardio
    login_required = True
    output_serializer = CardioOutputSerializer

class CardioUpdate(PostView):
    model = Cardio
    login_required = True
    optional_fields = ["name","description","goal","complete","measurement"]
    output_serializer = CardioOutputSerializer
    action_serializer = CardioUpdateSerializer

class CardioDelete(PostView):
    model = Cardio
    login_required = True
    output_serializer = CardioOutputSerializer
    action_serializer = CardioDeleteSerializer
