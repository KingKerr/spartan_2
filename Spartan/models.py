from django.db import models
from django.contrib.auth.models import AbstractUser

# Here are my models

class User(AbstractUser):
    favorite_fitness_hobby = models.CharField(max_length=50, help_text="Basketball, Yoga, Dancing")
    profile_image = models.ImageField(upload_to="user_profile", null=True, blank=True, height_field=None,
    width_field=None)
    goal = models.CharField(max_length=30, help_text="ex: Increase Lean Muscle, Lower Bodyfat, Improve Strength")

    def __unicode__(self):
        return str(self.username)

class Workout(models.Model):
    upper_body = models.CharField(max_length=30, help_text="ex: Bench Press, Shoulder Press, Shrugs")
    lower_body = models.CharField(max_length=30, help_text="ex: Squats, Lunges, Deadlifts")
    explosive = models.CharField(max_length=30, help_text="ex: Hang Cleans, Box Jumps, Hang Snatch")
    cardio = models.CharField(max_length=30, help_text="ex: Jogging, Cycling, 110s")
    speed = models.CharField(max_length=30, help_text="ex: Sprints, 10 yard starts, Speed Sled")
    skill = models.CharField(max_length=30, help_text="ex: Boxing, Jump Shooting, Route Running")
    athlete = models.ForeignKey(User, related_name='athlete')

    def __str__(self):
        return str(self.athlete)


class Meal(models.Model):
    breakfast = models.CharField(max_length=30, help_text="ex: Fruit and Oatmeal, Bacon & Eggs, Smoothie")
    lunch =  models.CharField(max_length=30, help_text="ex: Tuna Fish, Shrimp Salad, Chicken & Rice")
    dinner = models.CharField(max_length=30, help_text="ex: Steak & Baked Potato, Spaghetti & Meatballs, Red Beans & Rice")
    daily_caloric_intake = models.IntegerField(null=True)
    goal = models.CharField(max_length=30, help_text="ex: Increase Protein, Eat less starch, Eat more vegetables")
    daily_nutrition = models.ForeignKey(User, related_name='my_meals')

    def __unicode__(self):
        return u"{}".format(self.goal)



