from django import forms
from django.core import validators
from scheme_app.models import Scheme

class SchemeCreateForm(forms.ModelForm):
    class Meta:
        model=Scheme
        fields="__all__"

    def __init__(self,*args,**kwargs):
        super(SchemeCreateForm,self).__init__(*args,**kwargs)
        for visible in self.visible_fields():
            if 'class' in visible.field.widget.attrs:
                visible.field.widget.attrs['class']+=' form-control'
            else:
                visible.field.widget.attrs['class']='form-control'
