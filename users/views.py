from django.shortcuts import render, redirect
from django.views.generic import CreateView
from users.forms import UserCreateForm
from users.models import User
from django.urls import reverse_lazy



# Create your views here.

class UsercreateView(CreateView):
    model = User
    form_class = UserCreateForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy  ('core:home')




