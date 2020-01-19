from django.shortcuts import render
from .forms import GeneratePasswordForm


def index(request):
    """
    Вывод страницы с формой генерации пароля
    :param request:
    :return:
    """
    passwords = []

    if request.method == 'POST':
        form = GeneratePasswordForm(request.POST)

        if form.is_valid():
            passwords = form.get_password()
    else:
        form = GeneratePasswordForm

    return render(request, 'passwordgenerator/index.html', {
        'meta_title': 'Генератор паролей',
        'title': 'Генератор паролей',
        'form': form,
        'passwords': passwords
    })
