from rest_framework import viewsets
from django.http import JsonResponse
from rest_framework.authtoken.models import Token
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

def return_error(string):
    return JsonResponse({"Error": string})

def get_user_by_token(token):
    if token == None:
        return None
    else:
        token = token.replace("Token ", "")
        try:
            this_token = Token.objects.get(key=token).user
        except:
            return None

    return this_token

class BaseViewSet(viewsets.ViewSet):
    model = None
    output_serializer = None
    login_required = False

    @classmethod
    def list(self, request):
        if self.login_required == True:
            token = request.META.get('HTTP_AUTHORIZATION')
            user = get_user_by_token(token)
            if user == None:
                return return_error("login required")
        else:
            user = None

        if self.model == None:
            return return_error("View model is none")

        if self.output_serializer == None:
            return return_error("list Output serializer is none")

        objects = self.model.objects.all()
        if request.method == "GET":
            serializer = self.output_serializer(objects, many=True, context={'request': request})

            return JsonResponse(serializer.data, safe=False)

class PostView(viewsets.ViewSet):
    output_serializer = None
    action_serializer = None
    login_required = False
    required_fields = []
    optional_fields = []
    missing_fields = []

    @classmethod
    @csrf_exempt
    def action(self, request):

        if self.login_required == True:
            token = request.META.get('HTTP_AUTHORIZATION')
            user = get_user_by_token(token)
            if user == None:
                return return_error("login required")
        else:
            user = None

        if self.action_serializer == None:
            return return_error("No action serializer implemented")

        if request.method == "POST":
            request.user = user
            data = ["nothin"]

            if self.required_fields:
                try:
                    data = JSONParser().parse(request)
                except:
                    data = ["nothin"]

            verified_data = {}
            for field in self.required_fields:
                if field not in data:
                    return return_error("Missing field " + field)
                else:
                    verified_data.update({field: data[field]})

            for field in self.optional_fields:
                if field in data:
                    verified_data.update({field:data[field]})

            new_objects = self.action_serializer.action(request,verified_data)

            if "error" in new_objects:
                return return_error(new_objects["error"])

            if "success" not in new_objects:
                return return_error("Action Serializer must return dictionary with success key of new object(s) or error key with error string")

            serializer = self.output_serializer(new_objects["success"], many=True, context={'request': request})
            return JsonResponse(serializer.data, safe=False)

        else:
            return return_error("Must be POST request")

    @classmethod
    @csrf_exempt
    def update(self, request, pk):
        if self.login_required == True:
            token = request.META.get('HTTP_AUTHORIZATION')
            user = get_user_by_token(token)
            if user == None:
                return return_error("login required")
        else:
            user = None

        if self.action_serializer == None:
            return return_error("No action serializer implemented")

        if request.method == "POST":
            request.user = user
            data = ["nothin"]

            if self.required_fields or self.optional_fields:
                try:
                    data = JSONParser().parse(request)
                except:
                    data = ["nothin"]

            verified_data = {}
            for field in self.required_fields:
                if field not in data:
                    return return_error("Missing field "+field)
                else:
                    verified_data.update({field:data[field]})

            for field in self.optional_fields:
                if field in data:
                    verified_data.update({field:data[field]})

            new_objects = self.action_serializer.update(request,verified_data, pk)
            if "error" in new_objects:
                return return_error(new_objects["error"])

            if "success" not in new_objects:
                return return_error("Update Serializer must return dictionary with success key of new object(s) or error key with error string")

            serializer = self.output_serializer(new_objects["success"], many=True, context={'request': request})
            return JsonResponse(serializer.data, safe=False)

        else:
            return return_error("Must be POST request")

class GetView(viewsets.ViewSet):
    output_serializer = None
    action_serializer = None
    model = None
    login_required = False

    @classmethod
    def list(self, request):
        if self.login_required == True:
            token = request.META.get('HTTP_AUTHORIZATION')
            user = get_user_by_token(token)
            if user == None:
                return return_error("login required")
        else:
            user = None

        request.user = user

        if self.action_serializer == None:
            return return_error("No action serializer implemented")

        if request.method == "GET":
            if self.model == None:
                return return_error("View model is none")

            if self.output_serializer == None:
                return return_error("Output serializer is none")


            data = self.action_serializer.action(request)
            if "error" in data:
                return return_error(data["error"])

            objects = data["success"]
            if request.method == "GET":
                serializer = self.output_serializer(objects, many=True, context={'request': request})

                return JsonResponse(serializer.data, safe=False)

    @classmethod
    def update_many(self, request,pk):
        if self.login_required == True:
            token = request.META.get('HTTP_AUTHORIZATION')
            user = get_user_by_token(token)
            if user == None:
                return return_error("login required")
        else:
            user = None

        request.user = user

        if self.action_serializer == None:
            return return_error("No action serializer implemented")

        if request.method == "GET":
            data = self.action_serializer.update_many(request, pk)
            if "error" in data:
                return return_error(data["error"])

        objects = data["success"]
        resp = {}

        for serializer in self.output_serializer:
            ser = self.output_serializer[serializer]
            obj = objects[serializer]
            ser_obj = ser(obj, many=True, context={'request': request})
            resp.update({serializer:ser_obj.data})

        return JsonResponse(resp,safe=False)