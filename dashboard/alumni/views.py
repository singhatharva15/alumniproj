from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import auth
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from pyparsing import re
from certificate_template.cg import cg

from .models import *
from .forms import CareerForm, ProfileForm


# Profile view
@login_required
def profile(request):
    user= CustomUser.objects.all()
    return render(request,"index.html", {'newusers': user})

# update profile view
class UpdateProfile(UpdateView):
    model = CustomUser
    form_class = ProfileForm
    template_name = 'editprofile.html'
    success_url = reverse_lazy('home')

# career list and create view
class CareerCreateView(CreateView):
    model = Career
    form_class = CareerForm
    template_name = 'career.html'

    def get_context_data(self, **kwargs):
        kwargs['object_list'] = Career.objects.all()
        return super(CareerCreateView, self).get_context_data(**kwargs)

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self):
        messages.success(self.request, 'Recored Inserted Successfully')
        return reverse_lazy('career')


# experience update view
class UpdateExperice(UpdateView):
    model = Career
    form_class = CareerForm
    template_name = 'update-experience.html'

    def get_success_url(self):
        messages.success(self.request, 'Recored Inserted Successfully')
        return reverse_lazy('career', kwargs={'username': self.request.user.username})

# career delete view
@login_required
def destroyBatch(request, pk):  
    car = Career.objects.get(pk=pk)  
    car.delete()  
    messages.success(request, 'Recored Deleted Successfully')
    return redirect('career',)




@login_required
def events(request):
    even= Events.objects.all()
    return render(request,"events.html",{'events': even})


@login_required
def opportunity(request):
    opp= Opportunities.objects.all()
    return render(request,"opportunity.html",{'opps': opp})


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/home')

        else:
            messages.info(request,'Your Data is not registered. Contact Admin!')
            return redirect('/')

    else:
        return render(request,'registration/login.html')



def logout(request):
    auth.logout(request)
    return redirect('/')

# generate certificate
def generate_certificate(request):
    img = cg(request.user.username)
    response = HttpResponse(content_type="image/png")
    img.save(response, "PNG")
    return response