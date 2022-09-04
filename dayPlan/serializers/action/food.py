from rest_framework import serializers
from dayPlan.models import Food


class FoodUpdateSerializer(serializers.Serializer):
    @classmethod
    def update(self, request, data, pk):
        user = request.user

        try:
            food = Food.objects.get(id=pk)
        except:
            cardio = None

        if food == None:
            return {"error": "no lift with id "}

        if user != food.my_dayplan.user:
            return {"error": "this isn't your lift"}

        for field in data:
            setattr(food,field,data[field])

        food.save()
        return {"success":[food]}

class FoodDeleteSerializer(serializers.Serializer):
    @classmethod
    def update(self, request, data, pk):
        user = request.user

        try:
            food = Food.objects.get(id=pk)
        except:
            return {"error": "No Food with that id"}

        if food.my_dayplan.user!=user:
            return {"error":"Not your Food"}
        else:
            food.delete()
            return {"success":[food]}