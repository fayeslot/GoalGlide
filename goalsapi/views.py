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
@api_view(['GET'])
def goal_list(request):
    goals = Goal.objects.all()
    serializer = GoalSerializer(goals, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def goal_detail(request,pk):
    goals = Goal.objects.get(id-pk)
    serializer = GoalSerializer(goals, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def create_goal(request):
    serializer = GoalSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def update_goal(request,pk):
    goal = Goal.objects.get(id-pk)
    serializer = GoalSerializer(instance=goal,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def delete_goal(request,pk):
    goal = Goal.objects.get(id-pk)
    goal.delete()
    return Response("goal successfully deleted")
    
