from dataclasses import fields
from pyexpat import model
from django import forms
from django.forms import ModelForm,Textarea,HiddenInput,DateInput


from sacco1.models import members

class membersForm(forms.ModelForm):
    class Meta:
        model=members
        fields='__all__'
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for myField in self.fields:
            self.fields[myField].widget.attrs['class'] = 'form-control'


        

            




