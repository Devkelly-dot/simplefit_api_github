from rest_framework import serializers
from dayPlan.models import Cardio


class CardioUpdateSerializer(serializers.Serializer):
    @classmethod
    def update(self, request, data, pk):
        user = request.user

        try:
            cardio = Cardio.objects.get(id=pk)
        except:
            cardio = None

        if cardio == None:
            return {"error": "no lift with id "}

        if user != cardio.my_dayplan.user:
            return {"error": "this isn't your Cardio"}

        for field in data:
            setattr(cardio,field,data[field])

        cardio.save()
        return {"success":[cardio]}

class CardioDeleteSerializer(serializers.Serializer):
    @classmethod
    def update(self, request, data, pk):
        user = request.user

        try:
            cardio = Cardio.objects.get(id=pk)
        except:
            return {"error": "No Cardio with that id"}

        if cardio.my_dayplan.user!=user:
            return {"error":"Not your Cardio"}
        else:
            cardio.delete()
            return {"success":[cardio]}