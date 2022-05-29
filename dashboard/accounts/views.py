import os
from django.shortcuts import render
from django.conf import settings
from django.urls import reverse_lazy


from sesame.utils import get_query_string

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


from alumni.models import CustomUser as User

# Create your views here.
def magic_link(request):
    if request.POST:
        email = request.POST.get('email')
        if not email:
            return render(request, 'registration/magic-link.html', {"error": "Please enter valid email"}) 
    
        user, _ = User.objects.get_or_create(username=email.split('@')[0], email=email)
        token = get_query_string(user)

        message = Mail(
            from_email='sushilbhardwaj705@gmail.com',
            to_emails=email,
            subject='Magic Link',
            html_content=f"<strong>Magic link for login: {os.environ['HOST_NAME']}profile/{token}</strong>")
        try:
            sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
            response = sg.send(message)
            return render(request, 'registration/magic-link.html', {"res": True})
        except Exception as e:
            print(e.message)
    return render(request, 'registration/magic-link.html', {})