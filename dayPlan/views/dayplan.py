from rest_framework import viewsets

from dayPlan.serializers.output import DayplanOutputSerializer,LogOutputSerializer, LiftOutputSerializer, CardioOutputSerializer, FoodOutputSerializer
from dayPlan.serializers.action import LogDayplanSerializer, MyDayplansSerializer, DayplanAddLiftSerializer, DayplanAddCardioSerializer, DayplanAddFoodSerializer, DayplanGoalUpdateSerializer, DayplanGetPlanSerializer, DayplanClearSerializer, DayplanDeleteModelSerializer, DayplanClearModelSerializer

from dayPlan.models import Dayplan, Log, Lift, Cardio, Food
from .base import BaseViewSet
from .base import PostView, GetView

class DayplanViewSet(BaseViewSet):
    model = Dayplan
    login_required = True
    output_serializer = DayplanOutputSerializer

class LogDayplanViewSet(PostView):
    model = Log
    login_required = True
    output_serializer = LogOutputSerializer
    action_serializer = LogDayplanSerializer

class MyDayplansViewSet(GetView):
    model = Dayplan
    login_required = True
    output_serializer = DayplanOutputSerializer
    action_serializer = MyDayplansSerializer

class DayplanAddLift(PostView):
    model = Lift
    login_required = True
    required_fields = ["name","description","goal","weight","reps"]
    output_serializer = LiftOutputSerializer
    action_serializer = DayplanAddLiftSerializer

class DayplanAddCardio(PostView):
    model = Cardio
    login_required = True
    required_fields = ["name","description","goal"]
    output_serializer = CardioOutputSerializer
    action_serializer = DayplanAddCardioSerializer

class DayplanAddFood(PostView):
    model = Food
    login_required = True
    required_fields = ["name","description","complete"]
    output_serializer = FoodOutputSerializer
    action_serializer = DayplanAddFoodSerializer

class DayplanGoalUpdate(PostView):
    model = Dayplan
    login_required = True
    required_fields = ["goal"]
    output_serializer = DayplanOutputSerializer
    action_serializer = DayplanGoalUpdateSerializer

class DayplanGetPlan(GetView):
    model = Dayplan
    login_required = True
    output_serializer = {"dayplan":DayplanOutputSerializer,"food":FoodOutputSerializer,"cardio":CardioOutputSerializer,"lift":LiftOutputSerializer}
    action_serializer = DayplanGetPlanSerializer

class DayplanClear(PostView):
    model = Dayplan
    login_required = True
    required_fields = []
    output_serializer = DayplanOutputSerializer
    action_serializer = DayplanClearSerializer

class DayplanDeleteModels(PostView):
    model = Dayplan
    login_required = True
    required_fields = ["model"]
    output_serializer = DayplanOutputSerializer
    action_serializer = DayplanDeleteModelSerializer

class DayplanClearModels(PostView):
    model = Dayplan
    login_required = True
    required_fields = ["model"]
    output_serializer = DayplanOutputSerializer
    action_serializer = DayplanClearModelSerializer