from django import forms
from django.core import validators
from transaction_app.models import Transaction

class TransactionCreateForm(forms.ModelForm):
    class Meta:
        model=Transaction
        fields=['value','time_stamp','user_name']

    def __init__(self,*args,**kwargs):
        super(TransactionCreateForm,self).__init__(*args,**kwargs)
        for visible in self.visible_fields():
            if 'class' in visible.field.widget.attrs:
                visible.field.widget.attrs['class']+=' form-control'
            else:
                visible.field.widget.attrs['class']='form-control'
