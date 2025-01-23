from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from .forms import UserRegister


def valid_data(username, password, repeat_password, age, users):
    if username in users:
        return 'Пользователь уже существует'
    if password != repeat_password:
        return 'Пароли не совпадают'
    if int(age) < 18:
        return 'Вы должны быть старше 18'
    return None


# Create your views here.
def sign_up_by_django(request):
    users = ['Alexandr', 'Maria', 'Adam']
    info = {}
    context = {
        'info': info
    }
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']
            error = valid_data(username, password, repeat_password,
                               age, users)
            if error:
                info['error'] = error
                return render(request, 'registration_page.html', context)
            return HttpResponse(f'Приветствуем, {username}')
        else:
            info['form'] = UserRegister()
        return render(request, 'registration_page.html', info)


def sign_up_by_html(request):
    users = ['Alexandr', 'Maria', 'Adam']
    info = {}
    context = {
        'info': info
    }
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')
        error = valid_data(username, password, repeat_password,
                           age, users)
        if error:
            info['error'] = error
            return render(request, 'registration_page.html', context)
        return HttpResponse(f'Приветствуем, {username}')
    return render(request, 'registration_page.html', context)
