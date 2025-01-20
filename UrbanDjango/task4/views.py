from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
def main_page(request):
    title = 'Мой сайт'
    text = ' my text'
    context = {
        'games': ["Civilization V", "Atomic Heart", "Cyberpunk 2077"]
    }
    return render(request, 'platform.html', context)


def games_page(request):
    title = 'Игры'
    text = ' my text'
    context = {
        'games': ["Civilization V", "Atomic Heart", "Cyberpunk 2077"]
    }
    return render(request, 'games.html', context)


def shopping_page(request):
    title = 'Корзина'
    text = ' my text'
    context = {
        'games': ["Civilization V", "Atomic Heart", "Cyberpunk 2077"]
    }
    return render(request, 'cart.html', context)
