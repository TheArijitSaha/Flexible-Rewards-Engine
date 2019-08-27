from django import forms
from django.core import validators
from transaction_app.models import Transaction

class TransactionCreateForm(forms.ModelForm):
    class Meta:
        model=Transaction
        fields="__all__"
