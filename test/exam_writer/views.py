import json
from django.contrib.auth.forms import UserCreationForm
from django.http import StreamingHttpResponse, HttpRequest
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from .models import CustomUser

# Create your views here.
class SignUp(generic.CreateView):
	form_class = UserCreationForm
	success_url = reverse_lazy('login')
	template_name = 'signup/signup.html'

