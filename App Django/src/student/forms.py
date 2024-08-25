from django import forms

from .models import Students

class StudentForm(forms.Form):
    username = forms.CharField(required=False)
    password = forms.CharField()
    remember_me = forms.BooleanField()
    
class StudentsForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = ['first_name','last_name','date_of_birth','country','phone','scolarship','matricule']