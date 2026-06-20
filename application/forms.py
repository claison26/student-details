from django import forms
from .models import *
class ProductForm(forms.ModelForm):
    class Meta:
        model=Product
        fields='__all__'
        widgets={
        'name':forms.TextInput(attrs={'class':'form-control','style':'width:300px;'}),
        'age':forms.NumberInput(attrs={'class':'form-control','style':'width:300px;'}),
        }

class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields='__all__'
        widgets={
        'name':forms.TextInput(attrs={'class':'form-control','style':'width:300px;'}),
        'course':forms.TextInput(attrs={'class':'form-control','style':'width:300px;'}),
        'batch':forms.TextInput(attrs={'class':'form-control','style':'width:300px;'}),
        'staff':forms.TextInput(attrs={'class':'form-control','style':'width:300px;'}),
        'phone':forms.TextInput(attrs={'class':'form-control','style':'width:300px;'}),
        'domain':forms.TextInput(attrs={'class':'form-control','style':'width:300px;'}),
        }