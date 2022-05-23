from django.contrib import admin
from .models import *
from .forms import CustomUserCreationForm
from django.contrib.auth.admin import UserAdmin


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = CustomUserCreationForm

    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'Alumni Details',
            {
                'fields': (
                    'batch', 
                    'college',
                    'course_completed',
                    'mobile',
                    'certificate',
                    'career_opportunity',
                    'mentor_students',
                    'train_students',
                    'attend_events',
                     )
            }
        )
    )
# Register your models here.

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Events)
admin.site.register(Opportunities)
admin.site.register(Career)