from django.shortcuts import get_object_or_404, render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required 
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist 
from django.core.mail import send_mail
from goalsvine  import settings
from goals.forms import AddForm, GoalForm,AccountForm
from goals.models import  Goal
from django.db import transaction
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView


# Create your views here.
def home(requests):
    return render(requests, "goals/home.html")

def signup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        pass1 = request.POST.get("pass1")
        pass2 = request.POST.get("pass2")

        if User.objects.filter(email=email):
            messages.error(request, "Email already registered")
            return redirect('signup')
        
        if User.objects.filter(username=username):
            messages.error(request, "Username already exists")
            return redirect('signup')
        
        if pass1 != pass2:
            messages.error(request, "Passwords didn't match")
            return redirect('signup')

        myuser = User.objects.create_user(username,email,pass1)
        myuser.save()
        messages.success(request,"Your account has been successfully created")
        return render(request,"goals/goals.html")

    return render(request, "goals/signup.html")

def loginRegister(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('pass1')

        user = authenticate(username=username,password=password)

        if user != None:
            login(request,user)
            return render(request, "goals/dashboard.html")
        
        else:
            messages.error(request,"Invalid username or Password")
            return redirect("login")

        
    return render(request, "goals/signin.html")
@login_required()
def signout(request):
    logout(request)
    messages.success(request,"You have been logged out")
    return redirect("login")

@login_required()
def dashboard(request):
    goals = Goal.objects.filter(user = request.user)
    not_started_goals = Goal.objects.filter(user = request.user,status="NS").count()
    goals_in_progress = Goal.objects.filter(user = request.user,status="IP").count()
    completed_goals = Goal.objects.filter(user = request.user,status="C").count()

    context = { 
        'not_started_goals':not_started_goals,
        'goals_in_progress':goals_in_progress,
        'completed_goals':completed_goals,  
    }
    return render(request,"goals/dashboard.html",context)

@login_required()
def goals(request):
    not_started_goals = Goal.objects.filter(user = request.user,status = "NS")
    goals_inprogress = Goal.objects.filter(user = request.user,status = "IP")
    completed_goals = Goal.objects.filter(user = request.user,status = "C")
    
    context = {
        'not_started_goals':not_started_goals,
        'goals_inprogress':goals_inprogress,
        'completed_goals':completed_goals,
        'goals':goals,
        
    }
    return render(request,"goals/goals.html",context)

class GoalDetailView(DetailView):
    model = Goal
    template_name = "goals/goaldetail.html"

@login_required()
def update_goal(request, pk):
    goal = get_object_or_404(Goal, id = pk)
    
    if request.method == 'POST':
        form = GoalForm(request.POST)
        if form.is_valid():
            goal.name = form.cleaned_data['name']
            goal.status = form.cleaned_data['status_option']
            goal.visibility = form.cleaned_data['visibility']
            goal.target_date = form.cleaned_data['target_date']
            goal.save()
            return redirect('goal-detail', id=pk)
    else:
        initial_data = {
            'name': goal.name,
            'status': goal.status,
            'visibility':goal.visibility,
            'deadline': goal.target_date,
        }
        form = GoalForm(initial=initial_data)
    
    return render(request, 'goals/updategoal.html', {'form': form})

@login_required()
def addGoal(request):
    if request.method == 'POST':
        form = AddForm(request.POST)
        if form.is_valid():
            goal = form.save(commit=False)  # Save the form but don't commit yet
            goal.user = request.user  # Assign the logged-in user (assuming request.user is available)
            goal.save()  # Now commit the changes to the database
            messages.success(request, 'Goal added successfully!')  # Display success message (optional)
            return redirect('goals')  # Redirect to goals page after saving
        else:
            return render(request, 'goals/addgoal.html', {'form': form, 'error': 'Form is invalid'})
    else:
        form = AddForm()
    return render(request, 'goals/addgoal.html', {'form': form})


@login_required()
def deleteGoal(request, pk):
    goal = get_object_or_404(Goal, id=pk, user=request.user)
    goal.delete()
    messages.success(request, "Goal has been deleted")
    return redirect('goals')

@login_required()
def accounts_management(request):
    user_account =  request.user
    return render(request, 'goals/account.html', {'user_account': user_account})

@login_required()
def manage_accounts(request):
    user_account = request.user
    
    return render(request, 'goals/manage_account.html', {'user_account':user_account})

@login_required()
def delete_accounts(request):
    user_account = User.objects.get()
    user_account.delete()
    return redirect('accounts_management')
