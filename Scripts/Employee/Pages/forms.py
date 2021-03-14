from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta():
        model           =   Employee
        fields          =   '__all__'
        widgets          =   {
            'Ename':forms.TextInput(attrs={'class':'form-control','id':'Ename'}),
            'Esalary':forms.NumberInput(attrs={'class':'form-control','id':'Esalary'}),
        }