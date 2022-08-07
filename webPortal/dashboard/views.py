from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.


def index(request) -> HttpResponse:
    if request.user.is_authenticated and request.user.is_active:
        return render(request, "dashboard/index.html")
    else:
        return redirect("/account/login")
