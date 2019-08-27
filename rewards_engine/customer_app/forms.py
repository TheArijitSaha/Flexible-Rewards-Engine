from django import forms
from django.core import validators
from customer_app.models import Customer


class CustomerCreateForm(forms.ModelForm):
    class Meta:
        model=Customer
        exclude=("cur_rewards","max_red")
