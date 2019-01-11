from django.shortcuts import render, redirect
from django.http import HttpResponse
#from django.core.urlresolvers import reverse
from django.contrib.auth.forms import UserCreationForm


def signup(request):
    """signup
    to register users
    """
    if request.method == "POST":
        userform = UserCreationForm(request.POST)
        if userform.is_valid():
            userform.save()

            return redirect("signup_ok")

    elif request.method == "GET":
        userform = UserCreationForm()

    return render(request, "registration/signup.html", {"userform":userform,})
# Create your views here.
