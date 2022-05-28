from django.shortcuts import redirect, render
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth import login
from django.urls import reverse_lazy
import os

from sesame.utils import get_query_string, get_user
from django.core.cache import cache

from alumni.models import CustomUser as User

# Create your views here.
def magic_link(request):
    if request.POST:
        email = request.POST.get('email')
        if not email:
            return render(request, 'registration/magic-link.html', {"error": "Please enter valid email"}) 
    
        user, _ = User.objects.get_or_create(username=email.split('@')[0], email=email)
        token = get_query_string(user)

        print(f"Your link: {os.environ['HOST_NAME']}profile/{token}")
        res = send_mail(
            subject="Magic Link",
            message=f"Your link: {os.environ['HOST_NAME']}profile/{token}",
            from_email= settings.EMAIL_HOST_USER,
            recipient_list=[email],
            fail_silently=True,
        )
        return render(request, 'registration/magic-link.html', {"res": True})
    return render(request, 'registration/magic-link.html', {})