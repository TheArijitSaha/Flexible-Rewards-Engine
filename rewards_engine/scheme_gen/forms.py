from django import forms
from django.core import validators
# from scheme_gen.models import Eligibility,Conversion,Scheme
from scheme_gen.models import Scheme,Transaction,Customer

class SchemeCreateForm(forms.ModelForm):
    class Meta:
        model=Scheme
        fields="__all__"

class TransactionCreateForm(forms.ModelForm):
    class Meta:
        model=Transaction
        fields="__all__"

class CustomerCreateForm(forms.ModelForm):
    class Meta:
        model=Customer
        exclude=("cur_rewards","max_red")
