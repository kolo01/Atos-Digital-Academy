from django import forms

# Create your models here.
class User(forms.Form):
    pseudo_name = forms.CharField()
    password = forms.CharField()
    confirm_password = forms.CharField()