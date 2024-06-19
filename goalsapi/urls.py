from django.urls import path
from . import views

urlpatterns = [
    
    path("goal-list/",views.goal_list,name="goal-list"),
    path("create-goal/",views.create_goal,name="create-goal"),
    path("goal-detail/<str:pk>/",views.goal_detail,name="goal-details"),
    path("update-goal/<str:pk>/",views.update_goal,name="update-goal"),
    path("delete-goal/<str:pk>/",views.delete_goal,name="delete-goal"),
    
]