from django import forms
from random import choice


class GeneratePasswordForm(forms.Form):
    """
    Форма генерации пароля
    """
    digit_symbols = forms.BooleanField(label='цифры 0-9', required=False, label_suffix='', initial='checked')
    small_symbols = forms.BooleanField(label='маленькие буквы a-z', required=False, label_suffix='', initial='checked')
    big_symbols = forms.BooleanField(label='большие буквы A-Z', required=False, label_suffix='', initial='checked')
    special_symbols = forms.BooleanField(label='специальные символы (%, *, ), ?, @, #, $, ~)', required=False,
                                         label_suffix='')
    skip_doubles = forms.BooleanField(label='избегать повторяющихся символов', required=False, label_suffix='')
    skip_similar = forms.BooleanField(label='избегать похожие символы (i, l, 1, L, o, 0, O)', required=False,
                                      label_suffix='')
    count = forms.CharField(label='Количество паролей', required=False, label_suffix='', initial=6)
    length = forms.CharField(label='Длина пароля', required=False, label_suffix='', initial=12)

    def get_password(self):
        """
        Генерация пароля
        :return: Сгенерованный пароль
        """
        symbols = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                   'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
                   'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G',
                   'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
                   'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3',
                   '4', '5', '6', '7', '8', '9', '0']

        password_length = int(self.cleaned_data['length']) if self.cleaned_data['length'] else 12

        password = []

        for i in range(password_length):
            password.append(choice(symbols))

        return "".join(password)
