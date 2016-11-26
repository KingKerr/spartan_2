from django import forms
# noinspection PyUnresolvedReferences
from django.forms import ModelForm
from django.core.exceptions import ValidationError
from Spartan.models import User, Workout, Meal
from django.contrib.auth.forms import UserCreationForm
# noinspection PyUnresolvedReferences
from django.db import models

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2", "profile_image", "goal",
                  "favorite_fitness_hobby"]

    def clean_username(self):
        username = self.cleaned_data["username"]
        try:
            User.objects.get(username=username)

        except User.DoesNotExist:
            return username

        raise forms.ValidationError(
            self.error_messages['duplicate_username'],
            code="duplicate_username",
        )



# Beginning of Workout Form

class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ["upper_body",
                  "lower_body",
                  "explosive",
                  "cardio",
                  "speed",
                  "skill"
                  ]

# End of Workout Form

# Beginning of Meal Form

class MealForm(forms.ModelForm):
    class Meta:
        model = Meal
        fields = ["breakfast",
                  "lunch",
                  "dinner",
                  "daily_caloric_intake",
                  "goal"]

# End of Meal Form