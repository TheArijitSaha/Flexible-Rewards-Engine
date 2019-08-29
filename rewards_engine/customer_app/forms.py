from django import forms
from django.core import validators
from customer_app.models import Customer


class CustomerCreateForm(forms.ModelForm):
    class Meta:
        model   =   Customer
        fields  =   ["name"]
        widgets =   {
            'name'  :   forms.TextInput(attrs={
                'placeholder'   :   'Enter Name',
            }),
        }

    def __init__(self,*args,**kwargs):
        super(CustomerCreateForm,self).__init__(*args,**kwargs)
        for visible in self.visible_fields():
            if 'class' in visible.field.widget.attrs:
                visible.field.widget.attrs['class']+=' form-control'
            else:
                visible.field.widget.attrs['class']='form-control'
