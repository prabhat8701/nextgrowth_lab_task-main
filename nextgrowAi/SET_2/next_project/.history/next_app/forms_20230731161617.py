from django import forms
from django.contrib.auth.models import User
from next_app.models import Admin_User,Common_User

class Admin_User_Form(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model=User
        fields=['first_name','last_name','username','email','password']

class Admin_User_AddForm(forms.ModelForm):
    class Meta():
        model=Admin_User
        # fields='__all__'
        fields=['phone']

class Common_User_Form(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model=User
        fields=['first_name','last_name','username','email','password']

class Common_User_AddForm(forms.ModelForm):
    class Meta():
        model=Common_User
        # fields='__all__'
        fields=['phone1']


class AndroidAppForm(forms.ModelForm):
    class Meta:
        model = AndroidApp
        fields = ['name', 'points']