from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import User
from .forms import LoginForm

def main(request):
    return render(request, 'base/main.html')


def about_us(request):
    return render(request, 'base/about_us.html')


def loginPage(request):
    if request.user.is_authenticated:
        return redirect("main")

    if request.method == "POST":

        if request.user.is_authenticated:
            return redirect("main")

        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, email=cd['email'], password=cd['password'])

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect("main")
                else:
                    messages.error(request, 'Неактивный аккаунт')
            else:
                messages.error(request, 'Неверный e-mail или пароль')
    else:
        form = LoginForm()

    context = {'form' : form}
    return render(request, 'base/login_form.html', context=context)

def logoutPage(request):
    logout(request)
    return redirect("main")