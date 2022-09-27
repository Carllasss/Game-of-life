from django import forms


class CellForm(forms.Form):
    x = forms.IntegerField()
    y = forms.IntegerField()
