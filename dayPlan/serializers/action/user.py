from rest_framework import serializers
from django.http import JsonResponse
from dayPlan.models import User, Dayplan
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from django.db.models import Q

class CreateUserSerializer(serializers.Serializer):
    # create user and their 7 dayplans
    @classmethod
    def action(self, request, data):

        if(data["username"] == ""):
            return {"error":"Please enter a username"}
        if(data["email"] == ""):
            return {"error":"Please enter an email"}
        
        # CREATE THE USER OBJECT WITH HASHED PASS
        if User.objects.filter(Q(username=data["username"]) | Q(email=data["email"])):
            return {"error": "Username or email taken"}

        data["password"] = make_password(data["password"]) #hash the pass
        data["email"] = data["email"].lower()
        data["username"] = data["username"].lower()

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
        
class LoginUserSerializer(serializers.Serializer):
    @classmethod
    def action(self, request, data):
        password = data["password"]

        login_info = data.get("username_or_email")
        username = ""
        try:
            user = User.objects.get(email=login_info.lower())

        except ObjectDoesNotExist:
            try:
                user = User.objects.get(username=login_info.lower())
            except ObjectDoesNotExist:
                return {"error": "Couldn't login with those credentials"}
        
        username = user.username

        logged_in_user = authenticate(username=username,password=password)

        if(user != None):
            token, created = Token.objects.get_or_create(user=logged_in_user)
            return_object = {
                ""
            }
            return {"success":[{"key":token.key}]}
        else:
            return {"error":"Couldn't login with those credentials"}