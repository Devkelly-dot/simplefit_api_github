from dayPlan.serializers.output import UserOutputSerializer, TokenOutputSerializer
from dayPlan.serializers.action import CreateUserSerializer, LoginUserSerializer
from dayPlan.models import User
from rest_framework.authtoken.models import Token
from .base import PostView


class CreateUserView(PostView):
    model = User
    login_required = False
    required_fields = ["username","password","email"]
    output_serializer = UserOutputSerializer
    action_serializer = CreateUserSerializer

class LoginUserView(PostView):
    model = User
    login_required = False
    required_fields = ["username_or_email","password"]
    output_serializer = TokenOutputSerializer
    action_serializer = LoginUserSerializer