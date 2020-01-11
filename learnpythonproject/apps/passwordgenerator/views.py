from django.shortcuts import render


def index(request):
    return render(request, 'passwordgenerator/index.html', {
        'meta_title': 'Генератор паролей',
        'title': 'Генератор паролей'
    })
