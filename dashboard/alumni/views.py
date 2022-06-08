from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import auth
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from certificate_template.cg import cg

from alumni.models import Opportunities, Career, Events
from alumni.forms import CareerForm, ProfileForm
from accounts.models import User


# Profile view
@login_required
def profile(request):
    if request.user.is_authenticated:
        return render(request,"index.html", {})
    return redirect('login')

# update profile view
class UpdateProfile(UpdateView):
    model = User
    form_class = ProfileForm
    template_name = 'editprofile.html'
    success_url = reverse_lazy('profile')

    def get_success_url(self):
        messages.success(self.request, 'Profile Updated Successfully')
        return reverse_lazy('profile')


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
        return reverse_lazy('career')

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


# generate certificate
def generate_certificate(request):
    img = cg(request.user.email.split('@')[0])
    response = HttpResponse(content_type="image/png")
    img.save(response, "PNG")
    return response