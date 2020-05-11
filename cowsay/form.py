from django import forms

class AddCowsay(forms.Form):
    text = forms.CharField(max_length=50)