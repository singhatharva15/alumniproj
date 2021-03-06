from collections import UserDict
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import auth
from django.utils import timezone

# Create your models here.
class CustomUser(AbstractUser):
    batch = models.CharField(max_length=10)
    college = models.CharField(max_length=100)
    #email = models.EmailField(max_length=254, unique=True, db_index=True, primary_key=True)   
    course_completed = models.CharField(max_length=75)
    mobile = models.IntegerField(null=True)
    certificate = models.FileField(null=True)
    career_opportunity = models.BooleanField(default=False)
    mentor_students = models.BooleanField(default=False)
    train_students = models.BooleanField(default=False)
    attend_events = models.BooleanField(default=False)

    # USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ['username', 'mobile']

class Career(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    organization = models.CharField(max_length=150)
    position = models.CharField(max_length=150)
    s_date = models.DateField(auto_now=False, auto_now_add=False)
    e_date = models.DateField(auto_now=False, auto_now_add=False)
    present = models.BooleanField(default=False)

class Events(models.Model):
    event_name = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=100)
    Remark = models.TextField()


class Opportunities(models.Model):
    title = models.CharField(max_length=100)
    organization = models.CharField(max_length=100)
    criteria = models.CharField(max_length=100)
    remark = models.TextField()