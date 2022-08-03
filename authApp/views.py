import profile
import re
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.views.generic import (CreateView, DetailView, FormView, ListView, TemplateView, View)

from authApp.forms import LoginForm
from .models import *
# Create your views here.


class IndexView(TemplateView):
    template_name = 'main/index.html'




class LoginView(TemplateView):
    template_name = 'authpage/login.html'

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')
        print("________________________________")
        usr = authenticate(username=username, password=password)
        if usr is not None and UserProfile.objects.filter(user = usr).exists():
            login(self.request, usr, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('facebook:index')
            print("login")
        else:
            print("error")
            return render(self.request, self.template_name, {'error': 'invalid creditials'})


class SignUpView(TemplateView):
    template_name = 'authpage/signup.html'

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')
        firstname = request.POST.get('first_name')
        email = request.POST.get('email')
        lastname = request.POST.get('last_name')
        gender = request.POST.get('gender')
        birthday = request.POST.get('birthday')
        print("________________________________")
        if (User.objects.filter(username = username).exists() or User.objects.filter(email = email)):
            return render(self.request, self.template_name, {'error': 'Username already exist'})
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            profile = UserProfile(user=user, first_name=firstname, last_name=lastname, email=email, birthday=birthday, gender=gender)
            profile.save()
            return redirect('facebook:login')