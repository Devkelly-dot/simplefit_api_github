from rest_framework import serializers
from django.http import JsonResponse
from dayPlan.models import User, Dayplan
from django.contrib.auth.hashers import make_password
from rest_framework.authtoken.models import Token
from django.db.models import Q

class CreateUserSerializer(serializers.Serializer):
    # create user and their 7 dayplans
    @classmethod
    def action(self, request, data):

        # CREATE THE USER OBJECT WITH HASHED PASS
        if User.objects.filter(Q(username=data["username"]) | Q(email=data["email"])):
            return {"error": "Username or email taken"}

        data["password"] = make_password(data["password"]) #hash the pass
        user = User.objects.create(**data)

        # CREATE TOKEN
        if user:
            token = Token.objects.create(user=user)
        else:
            return {"error": "failed to create user and token"}

        # CREATE THE USER'S 7 DAYPLANS
        if user:
            for day in Dayplan.DayChoices:
                day_data = {"user": user}
                day_data.update({"day":day})
                day_object = Dayplan.objects.create(**day_data)

            return {"success":[user]}
        else:
            return {"error": "failed to create user and days"}