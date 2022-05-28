from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from .models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    # profile_image = forms.FileField()
    birth_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD')

    class Meta:
        model = User
        fields = ['username', 'email', 'birth_date', 'password1', 'password2']

# This will allow to update user name and email
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

# This will allow to update profile image
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']

# Change username label to Email
class CustomAuthenticationForm(AuthenticationForm):
    username = UsernameField(
        label='Email',
        widget=forms.TextInput(attrs={'autofocus': True})
    )
