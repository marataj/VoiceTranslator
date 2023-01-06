from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import LoginForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse
# Create your views here.

class LoginUser(View):
    def get(self, request):
        return render(request, "login.html", {"form": LoginForm()})

    def post(self, request):

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request,"Login successful", extra_tags="success")
            return HttpResponseRedirect(reverse("home"))
        # Redirect to a success page.
        
        else:
            messages.warning(request,"Wrong username or password", extra_tags="warning")
            return HttpResponseRedirect(reverse("login"))
        # Return an 'invalid login' error message.
    
class LogoutUser(View):
    def get(self, request):
        logout(request)
        messages.info(request,"User logged out")
        return HttpResponseRedirect(reverse("home"))

class RegisterUser(View):
    def get(self, request):
        return render(request, "register.html", {"form": UserCreationForm()})

    def post(self, request):
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            messages.info(request,"Registered successfuly", extra_tags="success")
            return HttpResponseRedirect(reverse("login"))
        else:
            messages.info(request,"Error", extra_tags="danger")

    

    
        

