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

    def __init__(self, *args, **kwargs):
        super(Survey, self).__init__(*args, **kwargs)
        self.fields['your_name'].required = False
        self.fields['frequency'].required = False
        self.fields['partday'].required = False
        self.fields['prefsport'].required = False
        self.fields['consume'].required = False
        self.fields['prodtype'].required = False
        self.fields['bodytype'].required = False
        self.fields['sex'].required = False
        self.fields['age'].required = False
        self.fields['email'].required = False
        self.fields['comment'].required = False