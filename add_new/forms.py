from django import forms

from test_bilet.models import *


class AddNewVopros(forms.ModelForm):
    class Meta:
        model = Vopros
        fields = '__all__'




