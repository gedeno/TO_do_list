from django import forms

class CreateNewlist(forms.Form):
    name = forms.CharField(label="name",max_length=300)
    cheak = forms.BooleanField()
