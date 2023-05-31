from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from api.models import UserProfile,Posts,Comments

class RegistrationForm(UserCreationForm):
    class Meta:
        password1=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
        password2=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
        model=User
        fields=["first_name","last_name","username","email","password"]
        widgets={
            "first_name":forms.TextInput(attrs={"class":"form-control"}),
            "last_name":forms.TextInput(attrs={"class":"form-control"}),
            "username":forms.TextInput(attrs={"class":"form-control"}),
            "email":forms.EmailInput(attrs={"class":"form-control"}),
            "password":forms.PasswordInput(attrs={"class":"form-control"})
        }

class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TimeInput(attrs={"class":"form-control"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))

class UserProfileForm(forms.ModelForm):
    class Meta:
        model=UserProfile
        fields=["profile_pic","bio","time_line_pic"]

class PostForm(forms.ModelForm):
    class Meta:
        model=Posts
        fields=["description"]

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comments
        fields=["comment"]
        

