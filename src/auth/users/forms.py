from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,SetPasswordForm

class SignUpForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "password1", "password2")
        
        
        
class ChangePasswordForm(SetPasswordForm):
    
    
    class Meta:
        model = User
        fields = ["new_password1","new_password2"]