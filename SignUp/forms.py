from django import forms
from django.contrib.auth.models import User
from SignUp.models import UserProfileInfo,User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User

        fields = ('username','first_name','last_name','email','password')

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('linkedin_url','profile_pic')
