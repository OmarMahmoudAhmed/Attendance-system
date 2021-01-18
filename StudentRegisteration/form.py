from django import forms
from django.db.models.base import Model
from .models import StudentRegisteration

class StudentRegisterationForm(forms.ModelForm):
    class Meta:
        model = StudentRegisteration
        fields = '__all__'
