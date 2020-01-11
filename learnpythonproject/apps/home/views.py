from django.shortcuts import render


def index(request):
    return render(request, 'base.html', {
        'meta_title': 'Полезные сервисы и приложения',
        'title': 'Python Learn Project'
    })
