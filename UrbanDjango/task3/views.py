from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
def main_page(request):
    title = 'Мой сайт'
    text = ' my text'
    context = {
        'title': title,
        'text': text,
    }
    return render(request, 'platform.html', context)


def games_page(request):
    title = 'Игры'
    text = ' my text'
    context = {
        'title': title,
        'text': text,
    }
    return render(request, 'games.html', context)


def shopping_page(request):
    title = 'Корзина'
    text = ' my text'
    context = {
        'title': title,
        'text': text,
    }
    return render(request, 'cart.html', context)
