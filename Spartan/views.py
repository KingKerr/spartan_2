from django.contrib.auth.decorators import login_required
# noinspection PyUnresolvedReferences
from .models import User, Workout, Meal
from django.shortcuts import render, redirect
from Spartan.forms import UserForm, WorkoutForm, MealForm
from django.contrib.auth import authenticate, login, logout
# noinspection PyUnresolvedReferences
from django.core.files.uploadhandler import FileUploadHandler
# noinspection PyUnresolvedReferences
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseRedirect
# noinspection PyUnresolvedReferences
from django.core.urlresolvers import reverse_lazy
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.

# This is for registration page


def sign_up(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password1']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'user/home.html')

    context = {
        'form': form,
    }

    return render(request, 'registration/sign_up.html', context)
# End of registration view

# Login view
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password1']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
            # Whenever a user has a correct password and the user is "Active"
                login(request, user)
            # Redirect user to their dashboard
                return  render("user/home.html")
            else:
                return render("This account is not active!")

        else:
            return render("Your login credentials are invalid!")
    else:
        return render(request, 'registration/login.html')

# End of Login view



# This is for the home page where users go after logging in


def home(request):
    if not request.user.is_authenticated():
        return render(request, 'registration/login.html')
    else:
        workouts = Workout.objects.all
        meals = Meal.objects.all


        data = {
            'user': request.user,
            'workouts': workouts,
            'meals': meals,
        }

    return render(request, 'user/home.html', data)






# End of user's home page

# Beginning of User's Workout Page

def workout_form(request):
    if not request.user.is_authenticated():
        return render(request, 'registration/login.html')

    else:

        form = WorkoutForm() # Will be overridden if `is_valid` returns `False`
        if request.method == "POST":
            form = WorkoutForm(data=request.POST)
            if form.is_valid():
                workout = form.save(commit=False)
                workout.athlete = request.user
                workout.save()
            return redirect('/user/home.html')

    return render(request, 'user/workout_form.html',
              {'form': form})

# End of Workouts form


# Edit Workout
@login_required()
def edit_workout(request, workout_id):
    workout = Workout.objects.get(id= workout_id)
    data = {'workout_form': WorkoutForm()}
    if request.method == "POST":
        form = WorkoutForm(request.POST)
        if form.is_valid():
            Workout.objects.create(upper_body=form.cleaned_data['upper_body'],
                               lower_body=form.cleaned_data['lower_body'],
                               explosive=form.cleaned_data['end_date'],
                               cardio=form.cleaned_data['cardio'],
                               speed=form.cleaned_data['speed'],
                               athlete= request.user,
                               skill=form.cleaned_data['skill'])
            workout.delete()
            workouts = Workout.objects.filter(athlete=request.user)
            data = {
            'user': request.user,
            'workouts': workouts,
            }
            return render(request, 'user/home.html', data)

        else:
            data = {'workout_form': form}
            return render(request, 'user/workout_form.html', data)
    else:
        return render(request, "user/workout_form.html", data)

# End of Edit Meal

# Add Meals form here

def meal_form(request):
    if not request.user.is_authenticated():
        return render(request, 'registration/login.html')
    else:
        form = MealForm() # Will be overridden if `is_valid` returns `False`
        if request.method == "POST":
            form = MealForm(data=request.POST)
            if form.is_valid():
                meal = form.save(commit=False)
                meal.daily_nutrition = request.user
                meal.save()
            return redirect('/user/home.html')

    return render(request, 'user/meal_form.html',
              {'form': form})



# End of Meals form

# Edit Meals form
@login_required()
def edit_meal(request, meal_id):
    meal = Meal.objects.get(id = meal_id)
    data = {"meal_form": MealForm()}
    if request.method == "POST":
        form = MealForm(request.POST)
        if form.is_valid():
            Meal.objects.create(breakfast=form.cleaned_data['breakfast'],
                               lunch=form.cleaned_data['lunch'],
                               dinner=form.cleaned_data['dinner'],
                               daily_caloric_intake=form.cleaned_data['daily_caloric_intake'],
                               goal=form.cleaned_data['goal'],
                               daily_nutrition=request.user)
            meal.delete()
            meals = Meal.objects.filter(daily_nutrition=request.user)
            data = {
                'meals': meals,
            }
            return render(request, "user/home.html", data)
        else:
            data = {"meal": Meal, "form": form}
            return render(request, "user/meal_form.html", data)
    else:
        return render(request, "user/meal_form.html", data)

# End of Edit Meal
# Index View which will be the page you see when visiting site first

def index(request):
    return render(request, 'index.html')

# End of the index view

# Beginning of logout view
def logout_view(request):
    logout(request)
    return  HttpResponseRedirect("registration/logged_out.html")

# End of logout view

def password_reset(request):
    return render(request, 'registration/password_reset_form.html')

'''
def email():
    email = EmailMessage(
    'subject_message',
    'content_message',
    'sender smtp gmail' +'<sender@gmail.com>',
    ['receiver@gmail.com'],
    headers = {'Reply-To': 'contact_email@gmail.com' }
)
email.send()

'''
