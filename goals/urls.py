from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    path("home/",views.home, name="home" ),
    path("signup",views.signup,name="signup"),
    path("login",views.loginRegister,name="login"),
    path("signout",views.signout,name="signout"),
    path("dashboard",views.dashboard,name="dashboard"),
    path("list",views.goals,name="goals"),
    path('goaldetail/<slug:slug>/',views.GoalDetailView.as_view(),name = "goal-detail"),
    path('update-goal/<int:pk>/',views.update_goal,name = "update"),
    path('add-goal',login_required(views.addGoal),name = "add-goal"),
    path('delete-goal/<int:pk>/',views.deleteGoal,name = "delete-goal"),
    path("accounts",views.accounts_management,name="accounts_management"),
    path("add-accounts",views.add_accounts,name="add-accounts"),
    path("manage-accounts",views.manage_accounts,name="manage-accounts"),
    path("delete-accounts",views.delete_accounts,name="delete-accounts"),
]