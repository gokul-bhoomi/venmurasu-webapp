from django import forms

class NumberForm(forms.Form):
    number = forms.IntegerField(label='Enter Number', max_value=5054)