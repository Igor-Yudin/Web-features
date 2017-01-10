from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from django.urls import reverse
from . models import User
from . forms import UserRegistrationForm
from django.contrib.auth.decorators import login_required
# Create your views here.

class UserRegistrationView(CreateView):
	form_class = UserRegistrationForm
	model = User
	template_name_suffix = '_create_form'
	success_url = '/success/'

@login_required
def success(request):
	return render(request, 'accounts/success.html')