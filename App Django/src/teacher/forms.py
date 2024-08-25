from django import forms

# Create your forms here.
class Teacher(forms.Form):
    name = forms.CharField()
    last_name = forms.CharField()
    birth_date = forms.DateField()
    gender = forms.CharField()
    matricule = forms.CharField()
    courses = forms.CharField()
    number = forms.CharField()
    ville = forms.CharField()