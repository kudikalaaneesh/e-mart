from django import forms
from .models import Employee
from .models import Signup
from .models import products
from .models import mobile,oneplus,redmi

class EmployeeForm(forms.ModelForm):
     class Meta:
         model = Employee
         fields = "__all__"

class Signups(forms.ModelForm):
    
    class Meta:
        model = Signup
        fields = "__all__"

class admin(forms.ModelForm):
    class Meta:
        model = products
        fields="__all__"

class mobiles(forms.ModelForm):
    class Meta:
        model = mobile
        fields="__all__"

class oneplusForm(forms.ModelForm):
    class Meta:
        model=oneplus
        fields="__all__"

class redmiform(forms.ModelForm):
    class Meta:
        model=redmi
        fields="__all__"