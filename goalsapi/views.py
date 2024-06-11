from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required 
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse 
from goalsapi.serializers import GoalSerializer
from goalsvine  import settings
from goals.models import  Goal
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status 
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET', 'POST', 'DELETE'])
def goal_list(request):
    if request.method == 'GET':
        goals = Goal.objects.all()
        serializer = GoalSerializer(goals, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = GoalSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)