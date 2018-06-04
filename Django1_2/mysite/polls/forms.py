from django import forms
import datetime
from .models import Question
from .models import Employee


class EmployeeForm(forms.ModelForm):    
    class Meta:
        model = Employee
        fields = ('employee_name','job_title','hire_date',)

