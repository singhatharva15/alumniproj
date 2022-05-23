from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Career, CustomUser
from django.views.generic import CreateView
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = "__all__"


class ProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name',
                  'course_completed', 'batch', 'college')
        labels = {'first_name': '', 'last_name': '',
                  'course_completed': '', 'batch': '', 'college': ''}
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'course_completed': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'FST Course Completed'}),
            'batch': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Batch'}),
            'college': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'UG/PG College'}),


            # 'career_opportunity': forms.BooleanField(label= 'Career Opportunities'),
            # 'mentor_students': forms.BooleanField(),
            # 'train_students': forms.BooleanField(),
            # 'attend_events': forms.BooleanField(),

        }


class CareerForm(forms.ModelForm):
    class Meta:
        model = Career
        fields = ('account', 'organization', 'position', 's_date', 'e_date')
        labels = {'account': '' ,'organization': '',
                  'position': '', 's_date': '', 'e_date': ''}
        n = CustomUser.get_username
        widgets = {
            'account': forms.TextInput(attrs={'class': 'form-control', 'readonly':'', 'value': n}),
            'organization': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Organization'}),
            'position': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Position'}),
            's_date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Start Date'}),
            'e_date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'End Date'}),

        }
