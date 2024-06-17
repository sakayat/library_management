from django.shortcuts import render
from django.views.generic import FormView
from .forms import UserRegistrationForm
from django.urls import reverse_lazy
from django.contrib.auth import login, logout

# Create your views here.
class UserRegistrationView(FormView):
    form_class = UserRegistrationForm
    template_name = "registration.html"
    success_url = reverse_lazy("login")
    
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)
    
    

