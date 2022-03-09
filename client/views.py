from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def client_profile(request):
    user = request.user
    context = {'user': user}

    # выводим разные страницы для рабочих и клиентских аккаунтов
    if not user.is_client:
        return render(request, 'client/work_account_profile.html', context)

    context['client'] = user.client
    return render(request, 'client/client_profile.html', context)
