from django import forms # type: ignore
from django.utils import timezone
from django import forms

from goals.models import Goal



STATUS_CHOICES  = (
    ('NS','Not Started'),
    ('IP','In Progress'),
    ('C','Completed'),
)
VISIBILITY_CHOICES = (
    ('PUB','Public'),
    ('PRV','Private')
)

class GoalForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Give the name for the goal'}))
    status_option = forms.ChoiceField(widget=forms.Select(attrs={'placeholder':'In Progress'}), choices=STATUS_CHOICES)
    target_date = forms.DateTimeField(widget =forms.DateInput(attrs={'type': 'date'}))
    visibility = forms.ChoiceField(widget=forms.Select(attrs={'placeholder':'Public'}), choices=VISIBILITY_CHOICES)

    

class AccountForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Username'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'Email'}))
    password = forms.CharField(widget =forms.TextInput(attrs={'placeholder':'Confrim Password','type': 'password'}))
    confirm_password = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Confrim Password','type': 'password'}))

class AddForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Give the name for the goal'}))
    status_option = forms.ChoiceField(widget=forms.Select(), choices=STATUS_CHOICES)
    target_date = forms.DateTimeField(widget =forms.DateInput(attrs={'type': 'date'}))
    visibility = forms.ChoiceField(widget=forms.Select(), choices=VISIBILITY_CHOICES)

    class Meta:
        model = Goal
        fields = '__all__'
