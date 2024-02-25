from django import forms


class Survey(forms.Form):
    your_name = forms.CharField( max_length=100)
    frequency= forms.CharField( max_length=100)
    partday= forms.CharField( max_length=100)
    prefsport= forms.CharField( max_length=100)
    consume= forms.CharField( max_length=100)
    prodtype= forms.CharField( max_length=100)
    bodytype= forms.CharField( max_length=100)
    sex= forms.CharField( max_length=100)
    age= forms.CharField( max_length=100)
    email= forms.CharField( max_length=100)
    comment= forms.CharField( max_length=100)