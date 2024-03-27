from django.shortcuts import render
from rest_framework.parsers import JSONParser
from .models import Profiles
from django.http import JsonResponse
from .serializers import ProfileSerializer


# Create your views here.
def profile_list(request):
    if request.method == 'GET':
        my_profiles = Profiles.objects.all()
        my_ser = ProfileSerializer(my_profiles, many=True)
        return JsonResponse(my_ser, safe=False)
