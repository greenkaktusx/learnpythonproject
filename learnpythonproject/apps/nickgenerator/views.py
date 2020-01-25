from django.shortcuts import render
from .forms import GenerateNickForm


def index(request):
    """
    Вывод страницы с формой генерации ников
    :param request:
    :return:
    """

    return render(request, 'nickgenerator/index.html', {
        'meta_title': 'Генератор ников',
        'title': 'Генератор ников'
    })
