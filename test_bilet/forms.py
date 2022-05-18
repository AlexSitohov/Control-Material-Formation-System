from django import forms
from .models import *


class ViborVoprosov(forms.Form):
    count = forms.IntegerField(max_value=30, min_value=1, label="Количество билетов",
                               widget=forms.NumberInput(attrs={'type': 'number',
                                                               'value': "",
                                                               'style': 'font-size: x-large',
                                                               'class': 'form-control',}))
    lvl_1 = forms.IntegerField(max_value=20, min_value=1, label="Количество вопросов 1-го уровня сложности",
                               widget=forms.NumberInput(attrs={'type': 'number',
                                                               'value': "",
                                                               'style': 'font-size: x-large',
                                                               'class': 'form-control'}))
    lvl_2 = forms.IntegerField(max_value=20, min_value=1, label="Количество вопросов 2-го уровня сложности",
                               widget=forms.NumberInput(attrs={'type': 'number',
                                                               'value': "",
                                                               'style': 'font-size: x-large',
                                                               'class': 'form-control'}))
    lvl_3 = forms.IntegerField(max_value=20, min_value=1, label="Количество вопросов 3-го уровня сложности",
                               widget=forms.NumberInput(attrs={'type': 'number',
                                                               'value': "",
                                                               'style': 'font-size: x-large',
                                                               'class': 'form-control'}))
