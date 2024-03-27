from django.shortcuts import render
from rest_framework.parsers import JSONParser
from .models import Profiles
from django.http import JsonResponse
from .serializers import ProfileSerializer
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

@csrf_exempt
def profile_list(request):
    if request.method == 'GET':
        my_profiles = Profiles.objects.all()
        my_ser = ProfileSerializer(my_profiles, many=True)
        return JsonResponse(my_ser.data, safe=False)

    if request.method == 'POST':
        data = JSONParser().parse(request)
        my_ser = ProfileSerializer(data=data)
        if my_ser.is_valid():
            my_ser.save()
            return JsonResponse(my_ser.data, status=201)
        return JsonResponse(my_ser.errors, status=400)
