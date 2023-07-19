from django import forms

class EMGGraphForm(forms.Form):
    port = forms.CharField(label='Port', max_length=100)
    baud_rate = forms.IntegerField(label='Baud Rate')
