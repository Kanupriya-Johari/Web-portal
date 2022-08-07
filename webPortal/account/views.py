from django.shortcuts import render, redirect
from django.contrib import auth
from django.http import HttpResponse
from django.contrib.auth import get_user_model , logout
from django.contrib import messages

# Create your views here.


def loginHandler(request) -> HttpResponse:

    if request.method == "POST":
        sign_in_email = request.POST.get("email", None)
        sign_in_password = request.POST.get("password", None)

        if sign_in_email == None or sign_in_password == None:
            messages.add_message(request, messages.ERROR, "Unauthorized request")
            return HttpResponse("<h1>Something went wrong</h1>")

        userModel = get_user_model()

        try:
            user = userModel.objects.get(email=sign_in_email)
        except userModel.DoesNotExist:
            messages.add_message(
                request, messages.WARNING, "Incorrect email or password"
            )
            return render(request, "account/login.html")
        else:
            if user.check_password(sign_in_password) and user.is_active:
                auth.login(request, user)
                return redirect("/dashboard")

            messages.add_message(
                request, messages.WARNING, "Incorrect email or password"
            )
            return render(request, "account/login.html")
    else:
        return render(request, "account/login.html")


def forgot(request) -> HttpResponse:
    return render(request, "account/forgot.html")

def logoutHandler(request)->HttpResponse:
    logout(request)
    return redirect("/account/login")
