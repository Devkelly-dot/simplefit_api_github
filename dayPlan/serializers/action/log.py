from rest_framework import serializers
from dayPlan.models import Log

class LogSerializer(serializers.Serializer):
    @classmethod
    def action(self, request):
        user = request.user

        try:
            logs = Log.objects.filter(user=user.id)
            return {"success":logs}
        except:
            return {"error":"User has no dayplans"}