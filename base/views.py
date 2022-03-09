from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import User
from .forms import LoginForm, UserRegistrationForm
from client.models import Client


def main(request):
    # главная страница веб-приложения
    return render(request, 'base/main.html')


def about_us(request):
    # страница с информацией о проекте
    return render(request, 'base/about_us.html')


def registration_page(request):
    """
        регистрация нового пользователя
        с помощью формы UserRegistrationForm()
    """
    if request.user.is_authenticated:
        return redirect('main')

    form = UserRegistrationForm()

    # если пользователь отправил форму
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)

        # если форма заполнена корректно, то создаем нового пользователя, иначе выводим ошибку
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            # создаем объект client, если пользователь хочет клиентский функционал
            if user.is_client:
                client = Client(user=user)
                client.save()
            # происходит авторизация пользователя и перенаправление
            login(request, user)
            return redirect('main')
        else:
            messages.error(request, 'Произошла ошибка во время регистрации, попробуйте еще раз')

    context = {'form': form}
    return render(request, 'base/registration_page.html', context=context)


def login_page(request):
    """
        аутентификация и авторизация пользователя
        по email и паролю
    """
    # если пользователь уже авторизован, то перенаправляем на главную
    if request.user.is_authenticated:
        return redirect("main")

    form = LoginForm()

    if request.method == "POST":

        form = LoginForm(request.POST)

        # если пользователь корректно ввел форму, пытаемся авторизовать его
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, email=cd['email'], password=cd['password'])

            # если пользователь с такими данными нашелся, смотрим, есть ли у него доступ к сайту
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect("main")
                else:
                    messages.error(request, 'Неактивный аккаунт')
            else:
                messages.error(request, 'Неверный e-mail или пароль')

    context = {'form': form}
    return render(request, 'base/login_page.html', context=context)


def logout_page(request):
    """
        выход пользователя из аккаунта
    """
    logout(request)
    return redirect("main")
