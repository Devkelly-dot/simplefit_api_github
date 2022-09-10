from dayPlan.serializers.output import LogOutputSerializer
from dayPlan.serializers.action import LogSerializer
from dayPlan.models import Log
from .base import GetView

class MyLogViewSet(GetView):
    model = Log
    login_required = True
    output_serializer = LogOutputSerializer
    action_serializer = LogSerializer