from dayPlan.serializers.output import UserOutputSerializer
from dayPlan.serializers.action import CreateUserSerializer
from dayPlan.models import User
from rest_framework.authtoken.models import Token
from .base import PostView


class CreateUserView(PostView):
    model = User
    login_required = False
    required_fields = ["username","password","email"]
    output_serializer = UserOutputSerializer
    action_serializer = CreateUserSerializer