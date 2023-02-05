from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import View

from .forms import LoginForm

# Create your views here.


class LoginUser(View):
    """
    Class that represents the login view. It's responsible for displaying the login form and authenticating the user.

    """

    def get(self, request):
        """
        The GET method of the LoginUser View.

        Parameters
        ----------
        request : The HTTP request.

        """
        return render(request, "login.html", {"form": LoginForm()})

    def post(self, request):
        """
        The POST method of the LoginUser View.
        Function is responsible for authenticating the user with the submitted form.

        Parameters
        ----------
        request : The HTTP request

        """

        user = authenticate(
            request,
            username=request.POST["username"],
            password=request.POST["password"],
        )

        if user is not None:
            login(request, user)
            messages.success(request, "Login successful", extra_tags="success")
            return HttpResponseRedirect(reverse("home"))

        else:
            messages.warning(
                request, "Wrong username or password", extra_tags="warning"
            )
            return HttpResponseRedirect(reverse("login"))


class LogoutUser(View):
    """
    Class that represens the Logout view.

    """

    def get(self, request):
        """
        The GET method of the LogoutUser View.

        Parameters
        ----------
        request : The HTTP request.

        """
        logout(request)
        messages.info(request, "User logged out")
        return HttpResponseRedirect(reverse("home"))


class RegisterUser(View):
    """
    Class that represents registration view.
    It's responsible for displaying the registration form, and the user registration.

    """

    def get(self, request):
        """
        The GET method of the RegisterUser View.

        Parameters
        ----------
        request : The HTTP request.

        """
        return render(request, "register.html", {"form": UserCreationForm()})

    def post(self, request):
        """
        The POST method of the RegisterUser View.

        Parameters
        ----------
        request : The HTTP request.

        """
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            messages.info(request, "Registered successfuly", extra_tags="success")
            return HttpResponseRedirect(reverse("login"))
        else:
            return render(request, "register.html", {"form": form})
