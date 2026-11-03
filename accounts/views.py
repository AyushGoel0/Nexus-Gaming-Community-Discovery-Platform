from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render

from .forms import ProfileForm, RegistrationForm


def register(request: HttpRequest) -> HttpResponse:
    if request.user.is_authenticated:
        return redirect("accounts:profile")

    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("accounts:login")
    else:
        form = RegistrationForm()

    return render(request, "accounts/register.html", {"form": form})


def accounts_home(request: HttpRequest) -> HttpResponse:
    if request.user.is_authenticated:
        return redirect("accounts:profile")
    return redirect("accounts:login")


@login_required
def profile(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = ProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("accounts:profile")
    else:
        form = ProfileForm(instance=request.user)

    return render(request, "accounts/profile.html", {"form": form})
