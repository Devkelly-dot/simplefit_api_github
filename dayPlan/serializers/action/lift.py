from rest_framework import serializers
from dayPlan.models import Lift


class LiftUpdateSerializer(serializers.Serializer):
    @classmethod
    def update(self, request, data, pk):
        user = request.user

        try:
            lift = Lift.objects.get(id=pk)
        except:
            lift = None

        if lift == None:
            return {"error": "no lift with id "}

        if user != lift.my_dayplan.user:
            return {"error": "this isn't your lift"}

        for field in data:
            setattr(lift,field,data[field])

        lift.save()
        return {"success":[lift]}


class LiftDeleteSerializer(serializers.Serializer):
    @classmethod
    def update(self, request, data, pk):
        user = request.user

        try:
            lift = Lift.objects.get(id=pk)
        except:
            return {"error": "No Lift with that id"}

        if lift.my_dayplan.user!=user:
            return {"error":"Not your Lift"}
        else:
            lift.delete()
            return {"success":[lift]}
