from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import User


STATUS_CHOICES  = (
    ('NS','Not Started'),
    ('IP','In Progress'),
    ('C','Completed'),
)
VISIBILITY_CHOICES = (
    ('PUB','Public'),
    ('PRV','Private')
)
# Create your models here.
    
     
class Goal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    name = models.CharField(max_length=200)
    visibility = models.CharField(choices = VISIBILITY_CHOICES,max_length=20,default='Private')
    status = models.CharField(choices = STATUS_CHOICES,max_length=20,default='Not Started')
    target_date = models.DateTimeField()
    slug = models.SlugField()

    class Meta: 
        ordering = ('-target_date', ) 
    
    def __str__(self):
            return self.name
    
    def get_absolute_url(self):
        return reverse("goal-detail",kwargs={
             'slug':self.slug
        })
    



    

    

    