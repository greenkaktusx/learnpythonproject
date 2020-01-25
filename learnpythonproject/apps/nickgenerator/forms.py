from django import forms
from random import choice


class GenerateNickForm(forms.Form):
    """
    Форма генерации ника
    """
    first_symbol = forms.CharField(label='Первая буква ника', required=False, label_suffix='', initial=0)
    length = forms.CharField(label='Длина ника', required=False, label_suffix='', initial=6)
    different_case_symbols = forms.BooleanField(label='Буквы разного регистра', required=False, label_suffix='',
                                                initial='')