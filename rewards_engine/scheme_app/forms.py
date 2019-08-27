from django import forms
from django.core import validators
from scheme_app.models import Scheme

class SchemeCreateForm(forms.ModelForm):
    class Meta:
        model=Scheme
        fields="__all__"
