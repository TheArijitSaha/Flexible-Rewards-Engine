from django import forms
from django.core import validators
from customer_app.models import Customer


class CustomerCreateForm(forms.ModelForm):
    class Meta:
        model=Customer
        exclude=("current_rewards","date_of_creation","customer_id")
