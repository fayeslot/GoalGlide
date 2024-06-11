from django.urls import path
from . import views

urlpatterns = [
    #path("categorylist/",views.categoriesList, name="categorylist" ),
    path("goallist",views.goal_list,name="goallist"),
    
]