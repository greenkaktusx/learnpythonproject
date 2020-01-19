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

        # Цифры
        digit_symbols = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

        # Маленькие буквы ангийского алфавита
        small_symbols = [
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
        ]

        # Большие буквы английского алфавита
        big_symbols = [
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
            'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
        ]

        # Специальные символы
        special_symbols = ['%', '*', '(', ')', '?', '@', '#', '$', '~']

        # Похожие символы
        similar_symbols = ['i', 'I', 'l', 'L', '1', 'o', 'O', '0']

        # Длина пароля
        password_length = int(self.cleaned_data['length']) if self.cleaned_data['length'] else 12

        # Проверяем включенные параметры формы и формируем итоговый список символов,
        # из которых будет сформирован пароль
        symbols = []

        if self.cleaned_data['digit_symbols']:
            symbols.extend(digit_symbols)

        if self.cleaned_data['small_symbols']:
            symbols.extend(small_symbols)

        if self.cleaned_data['big_symbols']:
            symbols.extend(big_symbols)

        if self.cleaned_data['special_symbols']:
            symbols.extend(special_symbols)

        password = []

        for i in range(password_length):
            password.append(choice(symbols))

        return "".join(password)
