from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth import login, authenticate
from .forms import LoginForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
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
            return HttpResponseRedirect("/")
        # Redirect to a success page.
        
        else:
            messages.warning(request,"Wrong username or password", extra_tags="warning")
            return HttpResponseRedirect("/users")
        # Return an 'invalid login' error message.
        

