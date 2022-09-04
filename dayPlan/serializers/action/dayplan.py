from rest_framework import serializers
from dayPlan.models import Dayplan, Lift, Cardio, Food, Log
from django.apps import apps

import datetime

class LogDayplanSerializer(serializers.Serializer):
    # log the dayplan
    @classmethod
    def update(self, request, data, pk):
        user = request.user

        try:
            my_dayplan = Dayplan.objects.get(id=pk)
        except:
            my_dayplan = None

        if my_dayplan == None:
            return {"error":"no dayplan with id "}

        if user != my_dayplan.user:
            return {"error": "this isn't your dayplan"}

        data = {"user":user, "date":datetime.date.today()}
        calorie_count = 0
        calorie_goal = my_dayplan.goal
        calories = ""
        lifts = ""
        cardios = ""

        try:
            food_objects = Food.objects.filter(my_dayplan=my_dayplan.id)
        except:
            food_objects = []

        for food in food_objects:
            calorie_count+=food.complete

        calories = str(calorie_count) + " / "+str(calorie_goal)
        calorie = {"calories":calories}
        data.update(calorie)

        try:
            lift_objects = Lift.objects.filter(my_dayplan = my_dayplan.id)
        except:
            lift_objects = []

        for lift in lift_objects:
            if lifts != "":
                lifts+=","

            measurements = {"KG":"kg","LB":"lb"}
            lifts += lift.name + " "+str(lift.reps)+" reps - "+str(lift.weight)+" "+str(measurements[lift.measurement])+" : "+str(lift.complete)+" / "+str(lift.goal)+" sets complete"

        if lifts == "":
            lifts = "None"

        lift = {"lift":lifts}
        data.update(lift)

        try:
            cardio_objects = Cardio.objects.filter(my_dayplan = my_dayplan.id)
        except:
            cardio_objects = []

        for cardio in cardio_objects:
            if cardios != "":
                cardios+=","

            measurements = {"MN": "minutes", "ML": "miles"}
            cardios += cardio.name + ": "+str(cardio.complete)+" / "+str(cardio.goal)+" "+str(measurements[cardio.measurement])+" complete"

        if cardios == "":
            cardios = "None"

        cardio = {"cardio":cardios}
        data.update(cardio)

        log = Log.objects.create(**data)

        if log:
            return {"success": [log]}
        else:
            return {"error": "couldn't create log"}

class MyDayplansSerializer(serializers.Serializer):
    @classmethod
    def action(self, request):
        user = request.user

        try:
            dayplans = Dayplan.objects.filter(user=user.id)
            return {"success":dayplans}
        except:
            return {"error":"User has no dayplans"}

class DayplanAddLiftSerializer(serializers.Serializer):
    @classmethod
    def update(self, request, data, pk):
        user = request.user

        try:
            my_dayplan = Dayplan.objects.get(id=pk)
        except:
            my_dayplan = None

        if my_dayplan == None:
            return {"error": "no dayplan with id "}

        if user != my_dayplan.user:
            return {"error": "this isn't your dayplan"}

        data.update({"complete":0})
        data.update({"my_dayplan":my_dayplan})
        lift = Lift.objects.create(**data)
        return {"success":[lift]}

class DayplanAddCardioSerializer(serializers.Serializer):
    @classmethod
    def update(self, request, data, pk):
        user = request.user

        try:
            my_dayplan = Dayplan.objects.get(id=pk)
        except:
            my_dayplan = None

        if my_dayplan == None:
            return {"error": "no dayplan with id "}

        if user != my_dayplan.user:
            return {"error": "this isn't your dayplan"}

        data.update({"complete":0})
        data.update({"my_dayplan":my_dayplan})
        cardio = Cardio.objects.create(**data)
        return {"success":[cardio]}

class DayplanAddFoodSerializer(serializers.Serializer):
    @classmethod
    def update(self, request, data, pk):
        user = request.user

        try:
            my_dayplan = Dayplan.objects.get(id=pk)
        except:
            my_dayplan = None

        if my_dayplan == None:
            return {"error": "no dayplan with id "}

        if user != my_dayplan.user:
            return {"error": "this isn't your dayplan"}

        data.update({"my_dayplan":my_dayplan})
        food = Food.objects.create(**data)
        return {"success":[food]}

class DayplanGoalUpdateSerializer(serializers.Serializer):
    @classmethod
    def update(self, request, data, pk):
        user = request.user

        try:
            my_dayplan = Dayplan.objects.get(id=pk)
        except:
            my_dayplan = None

        if my_dayplan == None:
            return {"error": "no dayplan with id "}

        if user != my_dayplan.user:
            return {"error": "this isn't your dayplan"}

        my_dayplan.goal = data["goal"]
        my_dayplan.save()
        return {"success":[my_dayplan]}

class DayplanGetPlanSerializer(serializers.Serializer):
    @classmethod
    def update_many(self, request, pk):
        user = request.user

        dayplan = [Dayplan.objects.get(id=pk)]

        if dayplan == None:
            return {"error": "no dayplan with id "}

        if user != dayplan[0].user:
            return {"error": "this isn't your dayplan"}

        lifts = Lift.objects.filter(my_dayplan=pk)
        cardios = Cardio.objects.filter(my_dayplan=pk)
        foods = Food.objects.filter(my_dayplan=pk)


        data = {"dayplan":dayplan, "food":foods,"cardio":cardios,"lift":lifts}

        return {"success":data}

class DayplanClearSerializer(serializers.Serializer):
    @classmethod
    def update(self,request, data, pk):
        user = request.user

        dayplan = Dayplan.objects.get(id=pk)

        if dayplan == None:
            return {"error": "no dayplan with id "}

        if user != dayplan.user:
            return {"error": "this isn't your dayplan"}

        Cardio.objects.filter(my_dayplan=pk).delete()
        Lift.objects.filter(my_dayplan=pk).delete()
        Food.objects.filter(my_dayplan=pk).delete()

        return {"success":[dayplan]}

class DayplanDeleteModelSerializer(serializers.Serializer):
    @classmethod
    def update(self,request, data, pk):
        user = request.user

        dayplan = Dayplan.objects.get(id=pk)

        if dayplan == None:
            return {"error": "no dayplan with id "}

        if user != dayplan.user:
            return {"error": "this isn't your dayplan"}

        if "model" not in data:
            return {"error":"model is required"}

        if data["model"] not in ["Lift", "Cardio", "Food"]:
            return {"error":"Model must be Lift, Cardio, or Food"}

        try:
            model = apps.get_model('dayPlan',data['model'])
        except:
            return {"error":"No model: "+data["model"]}

        model.objects.filter(my_dayplan=pk).delete()

        return {"success":[dayplan]}

class DayplanClearModelSerializer:
    @classmethod
    def update(self,request, data, pk):
        user = request.user

        dayplan = Dayplan.objects.get(id=pk)

        if dayplan == None:
            return {"error": "no dayplan with id "}

        if user != dayplan.user:
            return {"error": "this isn't your dayplan"}

        if "model" not in data:
            return {"error":"model is required"}

        if data["model"] not in ["Lift", "Cardio"]:
            return {"error":"Model must be Lift or Cardio"}

        try:
            model = apps.get_model('dayPlan',data['model'])
        except:
            return {"error":"No model: "+data["model"]}

        model.objects.filter(my_dayplan=pk).update(complete=0)

        return {"success":[dayplan]}