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

        # Количество паролей
        count_passwords = int(self.cleaned_data['count']) if self.cleaned_data['count'] else 6

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

        # Список сгенерированных паролей
        passwords = []

        for i in range(count_passwords):
            password = []

            for i in range(password_length):
                password_symbol = self.get_password_symbol(symbols, self.cleaned_data['skip_similar'],
                                                           self.cleaned_data['skip_doubles'], similar_symbols,
                                                           password, password_length)

                password.append(password_symbol)

            passwords.append("".join(password))
            password.clear()

        return passwords

    def get_password_symbol(self, symbols, similar, doubles, similar_symbols, password_symbols, password_length):
        """
        Получение символа для пароля

        :param symbols: Список символов для выбора
        :param similar: Флаг исключения похожих символов
        :param doubles: Флаг исключения одинаковых символов
        :param similar_symbols: Список похожих символов
        :param password_symbols: Список символов, отобранных ранее для пароля

        :return: Символ для пароля
        """
        password_symbol = choice(symbols)

        # Исключение похожих символов
        if similar:
            if password_symbol in similar_symbols:
                password_symbol = self.get_password_symbol(symbols, similar, doubles, similar_symbols,
                                                           password_symbols, password_length)

        # Исключение повторяющихся символов
        if doubles:
            if password_symbol in password_symbols and len(password_symbols) < len(symbols):
                symbols.remove(password_symbol)

                password_symbol = self.get_password_symbol(symbols, similar, doubles, similar_symbols,
                                                           password_symbols, password_length)

        return password_symbol
