from django.shortcuts import render, redirect
from django.http import HttpResponse
from account.models import Profile
from dashboard.models import Paper

# Create your views here.


def index(request) -> HttpResponse:

    if request.user.is_authenticated and request.user.is_active:
        get_profile = Profile()
        try:
            get_profile = Profile.objects.get(email=request.user.email)
        except get_profile.DoesNotExist:
            return render(request, "dashboard/index.html", {"profile": False})
        else:
            return render(request, "dashboard/index.html", {"profile": get_profile})
    else:
        return redirect("/account/login")


def papers(request) -> HttpResponse:
    if request.user.is_authenticated and request.user.is_active:
        get_profile = Profile()
        get_papers = Paper()
        try:
            get_profile = Profile.objects.get(email=request.user.email)
            get_papers = Paper.objects.filter(author=request.user)
        except get_profile.DoesNotExist or get_papers.DoesNotExist:
            return render(
                request, "dashboard/papers.html", {"profile": False, "papers": False}
            )
        else:
            return render(
                request,
                "dashboard/papers.html",
                {"profile": get_profile, "papers": get_papers},
            )
    else:
        return redirect("/account/login")


def patents(request) -> HttpResponse:
    if request.user.is_authenticated and request.user.is_active:
        return render(request, "dashboard/patents.html")
    else:
        return redirect("/account/login")
