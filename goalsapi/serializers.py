from django.forms import widgets
from rest_framework import serializers
from goals.models import  Goal
from django.contrib.auth.models import User


class GoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goal
        fields = ('user','name','target_date','visibility','status')

